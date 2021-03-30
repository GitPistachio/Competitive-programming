import os
import re
import urllib.parse


def nvl(value, replace_with):
    """Substitute a value when a None value encountered."""
    if value is None:
        return replace_with

    return value


def getProjectNameDetails(script):
    """Get details from project name comment."""
    project_search = re.search(r"(#|\*) *Project name *: *(.*)\n", script, re.IGNORECASE)
    if project_search is not None:
        project = project_search.group(2)
        *source, project_name = project.split(":")
        if len(source) == 1:
            source = (source[0].strip(), '')
        else:
            source = (source[0].strip(), source[1].strip())

        vals = project_name.split("-", 1)
        if len(vals) == 2:
            code, name = vals
            code = code.strip()
            name = name.strip()
        elif len(vals) == 1:
            code = None
            name = vals[0].strip()
        else:
            code = None
            name = None

        return (source, code, name)

    return (('', ''), None, None)


def getTagsDetails(script):
    """Get details from tags comment."""
    tags_search = re.search(r"\n(#|\*) *Tags *: *(.*)\n", script, re.IGNORECASE)
    if tags_search is not None:
        tags = list(map(lambda x: x.strip().lower().replace("  ", " "), tags_search.group(2).split(",")))

        return tags
    return []


def getLinkDetails(script):
    """Get details from link comment."""
    link_search = re.search(r"(#|\*) *Link *: *(.*)\n", script, re.IGNORECASE)
    if link_search is not None:
        link = link_search.group(2).strip()
        return link

    return None


def getTryItOnDetails(script):
    """Get details from try it on comment."""
    link_search = re.search(r"(#|\*) *Try it on *: *(.*)\n", script, re.IGNORECASE)
    if link_search is not None:
        link = link_search.group(2).strip()

    return link


def getProblemDetails(fname):
    """Get details from script comments."""
    fscript = open(fname, "r", encoding='utf-8')
    script = fscript.read()
    fscript.close()

    details = {}

    source, code, name = getProjectNameDetails(script)
    details["source"] = source
    details["code"] = code
    details["name"] = name

    tags = getTagsDetails(script)
    if len(tags) >= 1 and tags[0] in ("r", "c++", "bash", "c", "java", "python", "pypy", "brainfuck", "text"):
        if tags[0] == "pypy":
            details["lang"] = "python"
        elif tags[0] == "r":
            details["lang"] = "R"
        else:
            details["lang"] = tags[0]
        tags = tags[1:]
    else:
        file_extension = os.path.splitext(fname)[1]
        details["lang"] = getLangFromFileExtension(file_extension)

    details["tags"] = tags

    source_link = getLinkDetails(script)
    details["source_link"] = source_link

    try_it_on_link = getLinkDetails(script)
    details["try_it_on_link"] = try_it_on_link

    return details


def getLangFromFileExtension(file_extension):
    """Get programming language from file extension."""
    if file_extension == ".py":
        return "python"
    elif file_extension == ".java":
        return "java"
    elif file_extension == ".R":
        return "R"
    elif file_extension == ".sh":
        return "bash"
    elif file_extension == ".cpp":
        return "c++"
    elif file_extension == ".bf":
        return "brainfuck"


def getProblems():
    """Get all problems."""
    problems = []
    branches = ["CodeChef", "SPOJ", "Contests", "HackerRank"]
    start_dir = os.path.dirname(os.path.realpath(__file__))
    for branch in branches:
        for dirpath, dirs, files in os.walk(os.path.join(start_dir, branch)):
            for filename in files:
                fname = os.path.join(dirpath, filename)
                if re.search(r"\\__*", dirpath, re.IGNORECASE) or re.search(r"\\samples", dirpath, re.IGNORECASE) or filename in ['segment.py']:
                    continue

                # if filename != 'PLAY WITH MATH.R':
                #     continue

                problem_details = getProblemDetails(fname)
                if branch == 'Contests':
                    problem_details["type"] = "contest"
                else:
                    problem_details["type"] = "practice"

                problem_details["fname"] = fname

                script_link = ("" +
                               dirpath.replace(start_dir, "").replace("\\", "/") +
                               "/" + filename)
                problem_details["script_link"] = urllib.parse.quote(script_link)
                problems.append(problem_details)
    return problems

def getUniqueSortedTags(problems):
    tags = set()
    for problem in problems:
        tags.update(problem['tags'])

    return sorted(tags)

def arangeProblemsByTag(problems):
    problems_by_tag = {}
    for problem in problems:
        for tag in problem['tags']:
            if tag in problems_by_tag:
                problems_by_tag[tag].append(problem)
            else:
                problems_by_tag[tag] = [problem]
    
    return problems_by_tag

def arangeProblemsBySource(problems):
    problems_by_source = {}
    for problem in problems:
        source = problem['source'][0]
        if source in problems_by_source:
            problems_by_source[source].append(problem)
        else:
            problems_by_source[source] = [problem]
    
    return problems_by_source

def getLangColor(lang):
    # print(lang)
    if lang == "python":
        return "#3572A5"
    elif lang == "java":
        return "#B07219"
    elif lang == "R":
        return "#198CE7"
    elif lang == "bash":
        return "#89E051"
    elif lang == "c++":
        return "#F34B7D"
    else:
        return "#EFEFEF"

def getProblemNameWithHref(problem):
    if problem['code'] is None:
        return "[<span style=\"color:{}\">{}</span>]({})".format(getLangColor(problem['lang']), problem['name'], problem['script_link']) 
    else:
        return "[<span style=\"color:{}\">{} - {}</span>]({})".format(getLangColor(problem['lang']), problem['code'], problem['name'], problem['script_link']) 

problems = getProblems()
problems_by_tag = arangeProblemsByTag(problems)
problems_by_source = arangeProblemsBySource(problems)

path = os.path.dirname(os.path.realpath(__file__))
filename = "README.md"
readme_file = open(os.path.join(path, filename), "w", encoding='utf-8')
readme_file.write("# Competitive programming\n\n")
readme_file.write("The repository of solutions to various problems from coding challenge websites. The solutions are developed by [Wojciech Raszka - GitPistachio](https://gitpistachio.com). The code of the solutions is well-formatted and many of solutions have explanatory comments. If you are missing some solution or you have any requests or questions please use contact form from above website.\n")
readme_file.write("## The solutions by tag\n\n")
for tag in sorted(problems_by_tag.keys()):
    if tag not in ['fast i/o', 'brute force']:
        readme_file.write("### {}\n".format(tag))
        for problem in problems_by_tag[tag]:
            readme_file.write("{}\n".format(getProblemNameWithHref(problem)))

readme_file.write("## The solutions by source\n\n")
for source in sorted(problems_by_source.keys()):
    readme_file.write("### {}\n".format(source))
    for problem in problems_by_source[source]:
        readme_file.write("{}\n".format(getProblemNameWithHref(problem)))

readme_file.close()