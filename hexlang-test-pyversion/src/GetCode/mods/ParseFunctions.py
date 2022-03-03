def ParseFunctions(code: list[str]) -> dict:
    count = 0
    functions = {}
    index_list = []
    
    # parse params
    for line in code:
        if line[0] and line[-1] == ":":
            line = line.replace(":", "").split(" ", 1)
            name = line[0]
            args = None
            if len(line) != 1:
                args = line[1].split(",")
            
            functions[name] = {
                "index": count,
                "args": args,
                "content": []
            }
            index_list.append(count)
            
        count += 1

    # parse end
    count = 0
    for name in functions:
        count += 1
        if count != len(index_list):
            functions[name]["end"] = index_list[count]
        else:
            functions[name]["end"] = len(code)
    
    # parse content
    for name in functions:
        index = functions[name]["index"]
        end = functions[name]["end"]
        for line in code[index+1:end]:
            line = line.split(" ",1)
            com_name = line[0]
            args = None
            if len(line) != 1:
                args = line[1].split(",")
            functions[name]["content"].append(
                (com_name, args)
            )
    
    # parse labels
    for name in functions:
        content = functions[name]["content"]
        functions[name]["labels"] = {}
        count = 0
        for com in content:
            if com[0][:2] == "::":
                functions[name]["labels"][com[0][2:]] = count
            count += 1
    
    # del end and index
    for name in functions:
        functions[name].pop("end", 1)
        functions[name].pop("index", 1)
    
    return functions