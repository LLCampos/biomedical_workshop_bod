# BOD 2017 Workshop

## Before: 

- [ ] Open http://bioportal.bioontology.org/ontologies/RADLEX/?p=classes
- [ ] Open http://bioportal.bioontology.org/annotator with "I have a fracture in my leg bone.”
- [ ] Open http://bioportal.bioontology.org/annotator with "I have two fractures in my legs bones.”
- [ ] Open http://www.lasige.di.fc.ul.pt/webtools/webanno3/login.html?0

## Talk

Now, as an introduction to the practical activity you’re going to do next and as an example of one application of Text Mining in the real world, we’re going to talk a little about Text Mining applied to Radiology Reports.

Radiology Reports are a type of Health Records that are a potential source of useful information about the human body and diseases, information than can be used to the development of new clinical diagnosis and treatments. However, because these reports are mostly written in free text, it’s hard to extract information from them automatically, since the human language is not easy for computers to understand. 

One way to help the machines understand the Reports is by annotating them with semantic information. For example, finding in the text terms related to radiology and giving them some meaning, including relationships with other terms. These annotations could then be used by some applications to extract useful information from the report. 

This could be done by using an ontology related to Radiology. First of all, does any one knows what is an ontology? An ontology is a way to represent a subset of the world which can then be used has a standardized way to communicate about that subset of the world. This is really abstract, I know. But you will see an ontology in a second. The main ontology related to radiology is RadLex. RadLex was initially developed for the purposes of indexing radiology reports for searching but since then it has been applied to other applications. How can RadLex then be useful? Let’s walk through an example. Here is a representation of the RadLex ontology.

[[Start demo in Bioportal](http://bioportal.bioontology.org/ontologies/RADLEX/?p=classes)]

Imagine that you have a Radiology report and there you have the word tibia. (search for the term “tibia”) Ok, if the computer has information about RadLex, now it knows that tibia is a long bone, which by itself is a bone organ, which is a organ with cavitated organ parts, etc. So, if this report is in a database and I search the database for reports containing information about “long bones”, this report will appear in the result, although it doesn’t have the words “long bones” in it. 

[End demo]

This is just an example. One task which is usually necessary to be done to use ontologies like Radlex is to annotate text with terms from the ontology. To annotate it means to find mentions of terms belonging to the ontology in the text. Let’s walk through an example. One really friendly tool that does this annotation task is BioPortal Annotator.

[[Start demo in Bioportal](http://bioportal.bioontology.org/annotator)]

(annotate “I have a fracture in my leg bone.” with RadLex) 

So, in this sentence, we have mentions of three terms from Radlex. We can say we have just annotated this sentence. 

[End demo]

So, annotation can an important task for the purposes of take useful information out of radiology reports. But not every annotator has the same quality. Let’s go back to Bioportal annotator. 

[[Start demo in Bioportal](http://bioportal.bioontology.org/annotator)]

(annotate “I have two fractures in my legs bones.” with RadLex)

Oh, now we only have one annotation. This annotator doesn’t consider lexical variations of the words, so it doesn’t consider “legs” a mention of the RadLex term “leg”. I had this problem during the work I’m doing in my master thesis and after some research I’ve found this nice tool named NOBLE Coder that claims to solve the problem. But this tool is not tested for RadLex terms. Today we’re going to test this tool. Usually, to test this kind of tools we compare the annotations done by the tool with annotations done by some experts in the field at hand. You are going to be our experts this evening. 

Using BioPortal’s annotations as a basis, you’re going to manually annotate some radiology reports with RadLex terms and then the aggregated annotations will be compared with the annotations of the tool and will see how this tool’s performance compares with expert’s performance and then discuss the results. To evaluate the NOBLE Coder performance we will calculate measures: Precision, Recall and F-Score. Precision will check how many of the annotations of the NOBLE Coder are also annotated by you. Recall will check how of your annotations NOBLE Coder also annotates. F-Score is the combination of both. 

For this we’re going to use a web application called Webanno. 

[[Start demo in Webanno](http://www.lasige.di.fc.ul.pt/webtools/webanno/welcome.html)]

Examples to show:
- Click on some annotations already done by BioPortal
- Annotate “abdominal” with “abdomen”, after confirming that "abdomen" it's a RadLex term
- Annotate "Hepatocellular carcinoma" to explain the guidelien that we only want to annotate the most specific term

I do not have an example here, but sometimes the annotation suggestions that you have in the interface are wrong. One example is when you have the term "hand" annotated in "on the other hand..."

[End demo in Webanno]

Beyond comparing your aggregated annotations with the annotations from a automatic tool, we will also make this a competition whose winner will be the person who makes annotations closer to the aggregated results. So, we are assuming here the wisdom of the crowd, the aggregated annotations are the better annotations. The person closer to it wins. 

So let's start?

[Start of activity]
