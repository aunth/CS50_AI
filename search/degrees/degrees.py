import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)
    if path:
        print(f"{len(path)} degrees of separation")
        for i in path:
            print(i)
    else:
        print("Not connected.")

def create_graph(source, target):
    queue = QueueFrontier()
    queue.add(source)
    checked_stars = set()
    graph = {}
    while not queue.empty():
        star = queue.remove()
        checked_stars.add(star)
        neighbors = neighbors_for_person(star)
        for i in neighbors:
            if i[1] in checked_stars:
                continue
            else:
                checked_stars.add(i[1])
            queue.add(i[1])
            try:
                graph[star].add(i[1])
            except KeyError:
                graph[star] = {i[1]}
            try: 
                graph[i[1]].add(star)
            except KeyError:
                graph[i[1]] = {star}
            if i[1] == target:
                return graph
    return graph


def find_path(graph, target, source):
    if graph == {}:
        return None
    result = []
    starting = {i: -1 for i in graph}
    parents = {i: None for i in graph}

    start = source
    starting[start] = 0
    queue = [start]
    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if starting[i] == -1:
                queue.append(i)
                starting[i] = starting[v] + 1
                parents[i] = v

    start = target
    path = [start]
    parent = parents[start]
    while not parent is None:
        path.append(parent)
        parent = parents[parent]

    for i in range(len(path)-1):
        stars = {path[i], path[i+1]}
        for j in movies:
            if stars & movies[j]["stars"] == stars:
                result.append(f"{i+1}: {people[path[i]]['name']} and {people[path[i+1]]['name']} starred in {movies[j]['title']}")
                break
    return result



def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    graph = create_graph(source, target)
    path = find_path(graph, target, source)
    
    return path


    # TODO
    raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()




