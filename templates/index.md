---
layout: page
title: Templates 
permalink: /templates/
---


## P1 template for the slides

At P1, you need to introduce your topics to everyone in 5min, and *only 5 slides are possible*:

1. Title, name + mentors
1. What problem will be solved? Or motivation
1. Related work: what has been done by others?
1. Main research questions
1. Your methodology: how do you plan on solving this problem?

If you want, use this [PPT template]({{ "p1.pptx" }}), but you're allowed to use any software you want.


## P2 template

The document for P2 is a research proposal that must contain all the elements listed in the template available in the [graduation manual]({{ "/rules/" | prepend: site.baseurl }}) (Appendix 2).
*Ignore* any template you get from the central BK system if different, they send these emails without realising that Geomatics doesn't have the same criteria.

You are free to write your project plan with the word processor of your choice (including LaTeX), as long as all the asked parts are present.
You can use that [simple LaTeX template](https://gist.github.com/hugoledoux/d16d5a4d397858ac745e38f9e8561657) as starting point.


We expect a project plan to be around 10-15 pages (maximum).
It should show that you clearly know the problem you plan to solve, and that you master the related work.
We expect you to present the methodology you will use to solve your scientific problem(s), and to present preliminary results.
Also, this is a scientific proposal, so references are mandatory (even if there is no specific section in the template).

As an example, here's a [good project plan from a previous year]({{ "/pdfs/example_gradplan_mulder.pdf" | prepend: site.baseurl }}).
It contains:

  - an introduction in which the relevance of the project and its place in the context of geomatics is described, along with a clearly-defined problem statement;
  - a related work section in which the relevant literature is presented and linked to the project;
  - the research questions are clearly defined, along with the scope (ie what you will *not* be doing);
  - overview of the methodology to be used;
  - time planning---having a [Gantt chart](https://en.wikipedia.org/wiki/Gantt_chart) is probably a better idea then just a list;
  - since specific data and tools have to be used, it's good to present these concretely, so that the mentors know that you have a grasp of all aspects of the project;
  - the references.

<!-- For the system, you need to write a *short version* (1-2 sentences per point) so that these details can be uploaded and be accessible by the chair person of your P2/P4/P5. -->
<!-- Do not upload the full project plan, this one is only for your mentors. -->


## Template for the final thesis (P4 & P5)

Officially, there is no template.
However, we have made a [LaTeX template](https://github.com/tudelftgeomatics/thesis_template) containing all the parts that are required (eg title page, copyright, abstract, acknowledgements, table of contents, list of figures, appendices, etc.) and is structured in such a way that most/all supervisors expect.
It looks like this:

[![](thesislatex.png)](https://github.com/tudelftgeomatics/thesis_template/raw/master/thesis.pdf)

Download the [full LaTeX source in one ZIP](https://github.com/tudelftgeomatics/thesis_template/archive/master.zip).

*It is not an official template and it is not mandatory to use it.*

Notice that the TU Delft has a [generic LaTeX template for report](https://intranet.tudelft.nl/fileadmin/Files/medewerkersportal/mc/huisstijl/Downloads/latex_newreport.zip), but it's rather buggy and must be modified for an MSc thesis.

You are of course allowed to use Word (or others), if you want.


### What should the thesis contain?

<!-- http://web.stanford.edu/~pmcmahon/ThesisWritingTips.pdf -->
While you're allowed to structure your thesis you way you like it, good theses usually roughly follow this structure:

##### 1. Introduction (~5 pages)

What is the scientific problem you are aiming to solve? Why is it important? And why is it relevant to Geomatics? (make sure what you intend to do is inline with the overall learning objectives of the Geomatics programme at TU Delft) 

What is the main research question that you plan to answer?

Also, an overview of the obtained results and an overview of the thesis should be given.

##### 2. Theoretical background & related work (~15 pages)

Overview of all the topics related to your main research question. 
Here you provide some context for the reader---when describing what others did, explain clearly how their work relates to yours.

It's also the place to explain to the reader the concepts that are necessary to understand the rest of the thesis.

##### 3. Methodology/Experimental design and development (~20 pages)

Describe what you did. Present the design of your experiments and/or present the algorithm/methodology you used to answer your research question.

Observe that it's better to separate the theory from the practice.
That is, if you developed a new algorithm/method to process 3D city models, first describe this algorithm from a conceptual point-of-view (with pseudo-code) without discussing implementation details. 
These details (eg language details, classes, bits and bytes, running time), should be presented and discussed in a separate part of the thesis (a chapter about the implementation of the methodology is possible for instance).

##### 4. Implementation and Experiments  (~10 pages)

Details of the experiments (including datasets used) and of the implementation of the methodology developed. 

##### 5. Results and Analysis  (~10 pages)

Present your results, and provide an analysis of them.

##### 6. Conclusion, discussion and future work (∼5 pages)

Summarise your main result and give a clear answer to the research question you defined in the Introduction.
Discuss what did not work too.
Give an overview of new research questions that arose during your research, or promising ideas you had but didn't have time to investigate.

#####  7.  Appendices
 
Put here any material that would break the flow of the thesis: details about datasets, UML diagrams, list of tools and configurations used, etc.
It's possible that you have no appendix at all for your thesis.

Code you wrote should not be put in your thesis as an appendix.
No one wants to read hundreds of lines of code on paper.
Instead, put the code on a publicly accessible repository (eg GitHub) and give a link to the readers.
