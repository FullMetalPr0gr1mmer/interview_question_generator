'''usink Yake for skill extraction'''
import yake
def extract_skills(text,max_skills=10):
    kw_extractor=yake.KeywordExtractor(lan="en",n=3, top=max_skills,dedupLim=0.9)
    kws=kw_extractor.extract_keywords(text)
    return [kw for kw,scores in kws]
'''
yake lightweight, fast, unsupervised liberary 
and works great for extracting key phrases
from short text like resumes and job descriptions

here we extract skills(main pointes based on yake scores)
u recieve text as a string  and max skills (number of main points) u want back from the string)

make an object out of yake.KeywordExtractor
n=3 -> 3 words/skill(main point)
top= max_skills ->number of main points u want back from the string
dedupLim=0.9 -> similarity between 2 keywords treshold removal

the we return keywords only without their scores
'''