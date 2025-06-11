class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.title().split()
        for i in range(len(title)):
            if len(title[i])<3:
                title[i]=title[i].lower()
        return " ".join(title)