#!python
import os
import re


def nvl(x, y):
    if x is None:
        return y

    return x


def getProjectNameDetails(script):
    """Get details from project name comment."""
    project_search = re.search(r".*(#|\*) *Project name *: *(.*)\n", script, re.IGNORECASE)
    if project_search is not None:
        project = project_search.group(2)
        source, project_name = project.split(":")
        source = source.strip()

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

    return (None, None, None)


def getTagsDetails(script):
    """Get details from tags comment."""
    tags_search = re.search(r".*(#|\*) *Tags *: *(.*)\n", script, re.IGNORECASE)
    if tags_search is not None:
        tags = list(map(lambda x: x.strip().lower().replace("  ", " "), tags_search.group(2).split(",")))

        return tags
    return []


def getLinkDetails(script):
    """Get details from link comment."""
    link_search = re.search(r".*(#|\*) *Link *: *(.*)\n", script, re.IGNORECASE)
    if link_search is not None:
        link = link_search.group(2).strip()
        return link

    return None


def getTryItOnDetails(script):
    """Get details from try it on comment."""
    link_search = re.search(r".*(#|\*) *Try it on *: *(.*)\n", script, re.IGNORECASE)
    if link_search is not None:
        link = link_search.group(2).strip()

    return link


def getScriptDetails(script):
    """Get details from script comments."""
    details = {}

    source, code, name = getProjectNameDetails(script)
    details["source"] = source
    details["code"] = code
    details["name"] = name

    tags = getTagsDetails(script)
    if len(tags) >= 1:
        if tags[0] in ("R", "c++", "bash", "c", "java", "python", "pypy"):
            details["lang"] = tags[0]
            tags = tags[1:]
    details["tags"] = tags

    source_link = getLinkDetails(script)
    details["source_link"] = source_link

    try_it_on_link = getLinkDetails(script)
    details["try_it_on_link"] = try_it_on_link

    return details


def getLangFromFileExtension(file_extension):
    """Get programming language from file extension."""
    if file_extension == "py":
        return "python"
    elif file_extension == "java":
        return "java"
    elif file_extension == "R":
        return "R"
    elif file_extension == "sh":
        return "bash"
    elif file_extension == "cpp":
        return "c++"
    elif file_extension == "bf":
        return "brainfuck"


problems = []
start_dir = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(start_dir + "\\SPOJ\\"):
    for filename in files:
        name, extension = os.path.splitext(filename)
        script_file = open(os.path.join(root, filename), "r", encoding='utf-8')

        details = getScriptDetails(script_file.read()[:1500])
        details["script_link"] = ("https://github.com/GitPistachio/Competitive-programming/blob/master/SPOJ/" +
                                  os.path.basename(os.path.normpath(root)) + "/" + filename)

        problems.append(details)
        script_file.close()

path = os.path.dirname(os.path.realpath(__file__))
filename = "README.md"
readme_file = open(os.path.join(path, filename), "w", encoding='utf-8')
readme_file.write("# Competitive programming\n\n")
readme_file.write("## Solved practice problems on SPOJ\n\n")
for details in problems:
    title = nvl(details["code"], "None") + " - " + nvl(details["name"], "None")
    readme_file.write(title + "  \n")
readme_file.close()