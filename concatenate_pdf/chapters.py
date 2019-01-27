import concatenate

chapters = ["Chapter{}.pdf".format(n) for n in range(3,12)]

concatenate.concatenate("Chapter1.pdf", "Chapter2.pdf", 2)
for chapter in chapters:
    concatenate.concatenate("final.pdf", chapter, 2)