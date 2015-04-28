import re

temp="" 
#Just need to change the route of READ!
with open('/Users/haoyang/Desktop/circuit.v') as f:
#Below do not need to change any codes
    for line in f:
		if re.match('DFF', line):
			real_position=line.index(',')
			logic_position=real_position+1
			line=line[:logic_position] + ' .' + 'SE(SE)' + ', ' + 'SI(' + temp +')' + ',' + line[logic_position:]
			line_changed = line.replace('DFF', 'S_DFF')
			with open('/Users/haoyang/Desktop/newCircuit.v', 'a') as logic_f:
				logic_f.write(line_changed)
			pattern=re.search('.Q\((.*?)\)\);', line_changed)
			if pattern:
				value=pattern.group(1)
				temp=value
		else :
			with open('/Users/haoyang/Desktop/newCircuit.v', 'a') as logic_f:
				logic_f.write(line)
