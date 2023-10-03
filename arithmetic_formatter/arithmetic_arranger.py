def arithmetic_arranger(problems, is_enabled=False):
  arranged_problems = []
  firstLine = ""
  secondLine = ""
  thirdLine = ""
  forthLine = ""
  if len(problems > 5):
    return ('Error: Too many problems.')

  for problem in problems:
    arg = problem.split()

    if len(arg) != 3:
      return ('Error: Too many problems.')
    if arg[1] not in ("+", "-"):
      return ("Error: Operator must be '+' or '-'.")
    if not arg[0].isdigit() or not arg[2].isdigit():
      return ('Error: Numbers must only contain digits.')
    if len(arg[0]) > 4 or len(arg[2]) > 4:
      return ('Error: Numbers cannot be more than four digits.')

    len1 = len(arg[0])
    len2 = len(arg[2])

    maxLen = max(len1, len2)
    margin = " " * 4

    firstLine += arg[0].rjust(maxLen + 2, " ") + margin
    secondLine += arg[1] + " " + arg[2].rjust(maxLen, " ") + margin
    thirdLine += "-" * maxLen + "--" + margin
    result = str(eval(problem))
    forthLine += result.rjust(maxLen + 2, " ") + margin
  arranged_problems.append(firstLine.rstrip())
  arranged_problems.append(secondLine.rstrip())
  arranged_problems.append(thirdLine.rstrip())
  if (is_enabled):
    arranged_problems.append(forthLine.rstrip())

  # Join the lines and return the result
  return "\n".join(arranged_problems)
