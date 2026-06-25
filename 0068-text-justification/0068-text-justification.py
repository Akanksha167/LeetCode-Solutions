class Solution:
	
    __slots__ = ()
	
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
	    # Init return array in which, we'll store justified lines
        lines = []
		# current line width
        width = 0
		# current line words
        line = []
        
        for word in words:
			
            if (len(word) + width + len(line)) <= maxWidth:
                width += len(word)
                line.append(word)
                continue
            
			
            if len(line) == 1:
				
                lines.append(
                    "{0: <{width}}".format( " ".join(line), width=maxWidth)
                )
            else:
			  
                space, extra = divmod(
                    maxWidth - width,
                    len(line) - 1
                )
                
                i = 0
				
                while extra > 0:
                    line[i] += " "
                    extra -= 1
                    i += 1
                
				# Join line array into a string by common spaces, and append to justified lines.
                lines.append(
                    (" " * space).join(line)
                )
            
			
            line = [word]
            width = len(word)
        
		
        lines.append(
            "{0: <{width}}".format(" ".join(line), width=maxWidth)
        )
        
        return lines