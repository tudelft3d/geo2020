---
layout: page
title: Templates 
permalink: /templates/
---

## P2 template

The template in the graduation manual is the one you should follow (see Appendix 2, or get it directly [there](http://studenten.tudelft.nl/fileadmin/Files/studentenportal/os/BKspecifiek/Graduation_Plan_Template_Geomatics.docx)).
*Ignore* any template you get from the central BK system if different, they send these emails without realising that Geomatics doesn't have the same criteria.

The document for P2 is a research proposal that must contain all the elements listed in the template.
You are however free to write it with the word processor of your choice (including LaTeX), as long as all the sections are present (you are allowed to add sub-sections).
Also, this is a scientific proposal, so references are mandatory (even if there is no specific section in the template).

We expect a project plan to be around 10-15 pages.
It should show that you clearly know the problem you will aim at solving, and that you master the related work.
We expect you to present the methodology you will use to solve your scientific problem(s), and to present preliminary results.
<!-- You should however have a crystal-clear idea of what you will do, with what methodology, and the pitfalls that you will encounter. -->


## Template for the final thesis (P4 & P5)

Officially there is no template.
However, we have made a [LaTeX template](https://github.com/tudelftgeomatics/thesis_template) containing all the parts that are required (eg title page, copyright, abstract, acknowledgements, table of contents, list of figures, appendices, etc.) and is structured in such a way that most/all supervisors expect.
It looks like [this](https://github.com/tudelftgeomatics/thesis_template/raw/master/thesis.pdf).
*It is not an official template and it is not mandatory to use it.*

Notice that the TU Delft has a [generic template for report](https://intranet.tudelft.nl/fileadmin/Files/medewerkersportal/mc/huisstijl/Downloads/latex_newreport.zip), but it's rather buggy and must be modified for an MSc thesis.

You are of course allowed to use Word (or others), if you want.


### What should the thesis contain?

<!-- http://web.stanford.edu/~pmcmahon/ThesisWritingTips.pdf -->
While you're allowed to structure your thesis you way you like it, good theses (ie the ones that got hight marks) roughly follow this structure:

##### 1. Introduction (~7 pages)

What is the scientific problem you are aiming to solve? Why is it important? And why is it relevant to Geomatics? (make sure what you intend to do is inline with the overall learning objectives of the Geomatics programme at TU Delft) 

What is the main research question that you plan to answer?

##### 2. Theoretical background & related work (~15 pages)

Overview of all the topics related to your main research question. 
Here you provide some context for the reader---when describing what others did, explain clearly how their work relates to yours.

It's also the place to explain to the reader the concepts that are necessary to understand the rest of the thesis.

##### 3. Methodology/Experimental design (~25 pages)

Describe what you did. Present the design of your experiments and/or present the algorithm/methodology you used to answer your research question.

Observe that it's better to separate the theory from the practice.
That is, if you developed a new algorithm/method to process 3D city models, first describe this algorithm from a conceptual point-of-view (with pseudo-code) without discussing implementation details. 
These details (eg language details, classes, bits and bytes, running time), should be presented and discussed in a separate part of the thesis (a chapter about the implementation of the methodology is possible for instance).

##### 4. Experiments, results and analysis (~20 pages)

Present your results, details of the experiments (including datasets used) and provide an analysis of them.

##### 5. Conclusion, discussion and future work (∼5 pages)

Summarise your main result and give a clear answer to the research question you defined in the Introduction.
Discuss what did not work too.
Give an overview of new research questions that arose during your research, or promising ideas you had but didn't have time to investigate.

#####  6.  Appendices
 
Put here any material that would break the flow of the thesis: details about datasets, UML diagrams, list of tools and configurations used, etc.
It's possible that you have no appendix at all for your thesis.

Code you wrote should not be put in your thesis as an appendix.
No one wants to read hundreds of lines of code on paper.
Instead, put the code on a publicly accessible repository (eg GitHub) and give a link to the readers.
