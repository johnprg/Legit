### Legit or Misinformative

**Author**
John Rae-Grant

#### Executive summary

#### Rationale
There are few questions as important today as “should I believe this article”.  Indeed, with most people getting their “information” not from vetted sources, but from social media, the traditional methods of distinguishing trusted from untrusted sources have largely disappeared.  

Having access to a reasonably accurate real time measure of an article’s legitimacy could increase public media savvy, slow down viral spread of misinformation, and even potentially guide identification of deliberate disinformers.

#### Research Question
Can we classify a body of text (article, posting, email) as legitimate or misinformative?

#### Data Sources
For the proof of concept, we will use Wikipedia as the “fact” source and also as the source for test articles, paying particular attention to the citations and footnotes to provide outside sources.

#### Methodology
This will require leveraging some existing tech to:
Do Semantic Analysis: Identify assertions of fact in the target text.
Lookup and amend the Fact Repo: Do a vector search for matching assertions in the repo.
Store Metadata:  Build and store metadata for the article in the dataset used by the classifier.
The classifier itself will deliver a binary decision “legit” or “misinformative” based on the metadata, with a level of confidence for each classification.  I will compare different classifier models performance on the POC corpus.

#### Expected results
I expect that this will be similar to a spam filter.  It will perform well for articles which are more fact based and be heavily biased toward labelling articles as “misinformative”.
I am unsure about the availability of the existing tech described above, so that is a large x factor in putting this together.

#### Actual Results
What did your research find?

#### Next steps
What suggestions do you have for next steps?

#### Outline of project

- [Link to notebook 1]()
- [Link to notebook 2]()
- [Link to notebook 3]()


##### Contact and Further Information