ter = 'i+*()#'
nonter = 'EDTSF'
analysis_table = [
    [' ', 'i', '+', '*', '(', ')', '#'],
    ['E', 'TD', '', '', 'TD', '', ''],
    ['D', '', '+TD', '', '', 'ε', 'ε'],
    ['T', 'FS', '', '', 'FS', '', ''],
    ['S', '', 'ε', '*FS', '', 'ε', 'ε'],
    ['F', 'i', '', '', '(E)', '', ''],
]
stack_str = '#E'
ptr = 0
