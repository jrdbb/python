import difflib

if __name__ == '__main__':
    with open('base.txt') as base, open('target.txt') as target:
        baseLines = base.readlines()
        targetLines = target.readlines()
        unified_diff = difflib.ndiff(baseLines, targetLines)

    with open('output.html', 'w') as output:
        output.write(difflib.HtmlDiff(wrapcolumn=120).make_file(baseLines, targetLines, context=False))
