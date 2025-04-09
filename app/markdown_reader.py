class MarkdownReader:

    def __init__(self, text):
        self.text = text

    def goto(self, seq):
        i = self.text.find(seq)
        self.text = self.text[i:]

    def goto_nextrow(self):
        i = self.text.find("\n") + 1
        self.text = self.text[i:]

    def goto_list(self):
        self.goto("|-")
        self.goto_nextrow()

    def get_row_as_array(self):
        row = None
        while True:
            if self.text.strip() == "":
                return None
            
            i_br = self.text.find("\n") + 1
            row = self.text[:i_br]

            if row and row.strip() and not row.startswith("|-"):
                break
            self.goto_nextrow()

        array = row.split("|")
        array = [item.strip() for item in array if item.strip() not in ['', '\n']]
        
        self.text = self.text[i_br:]
        return array

    def prune_tail(self, seq):
        j = self.text.find(seq)
        self.text = self.text[:j]

    def print(self):
        print(self.text)