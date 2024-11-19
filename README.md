### Legit or Misinformative

**Author**
John Rae-Grant

#### Executive summary

The research question I sought to answer is "can we accurately classify a body of text (article, posting, email) as legitimate or misinformative?" I had originally intended to base this determination on metadata and semantic analysis, especially the fact density and provenance of the text, and to use Wikipedia as the source data.  In my research, I found that the labelling of articles on wikipedia was much more nuanced and subjective, and that the semantic parsing was too in depth of a specialized area to dive into.  Instead, I found several datasets of articles which had been labelled as "fake" or "real", and focused on building different NLP classifiers to see what level of accuracy could be achieved in matching the given labels.

#### Rationale
There are few questions as important today as “should I believe this article”.  Indeed, with most people getting their “information” not from vetted sources, but from social media, the traditional methods of distinguishing trusted from untrusted sources have largely disappeared.  

Having access to a reasonably accurate real time measure of an article’s legitimacy could increase public media savvy, slow down viral spread of misinformation, and even potentially guide identification of deliberate disinformers.

#### Research Question
Can we classify a body of text (article, posting, email) as legitimate or misinformative?

#### Data Sources
##### Kaggle
FakeNews - large dataset - 83500 samples - from https://www.kaggle.com/datasets/vishakhdapat/fake-news-detection
Base - smaller dataset - 9900 samples - from https://www.kaggle.com/datasets/nitishjolly/news-detection-fake-or-real-dataset

Both datasets contain text samples which have been labelled as 'Real' or 'Fake'.

#### Methodology
1. Train on existing datasets of news articles from two distinct sources, which labelled articles as "fake" or "real"
2. Experiment with several different types of classifiers, doing parameter searches on each to find the most accurate model of each type
3. Test the resulting winning models of each type with a sample of the other dataset as a test set.

#### Expected results
I expect that this will be similar to a spam filter.  It will perform well for articles which are more fact based and be heavily biased toward labelling articles as “misinformative”.
I am unsure about the availability of the existing tech described above, so that is a large x factor in putting this together.

#### Actual Results
The results were suprisingly encouraging!  All of the resulting models for both datasets and multiple sample sizes scored 90% or better accuracy.  

| Model         | Size | Dataset  | Best Score | Fit Time   |
|---------------|------|----------|------------|------------|
| Bayes         | 1980 | Base     | 0.974747   | 3.714640   |
| Bayes         | 2088 | FakeNews | 0.949102   | 3.897800   |
| Bayes         | 4177 | FakeNews | 0.958696   | 7.474342   |
| Bayes         | 4950 | Base     | 0.975505   | 9.496118   |
| Bayes         | 8354 | FakeNews | 0.957055   | 15.505293  |
| Bayes         | 9900 | Base     | 0.973737   | 20.876189  |
|               |      |          |            |            |
| Decision Tree | 1980 | Base     | 0.950758   | 3.763134   |
| Decision Tree | 2088 | FakeNews | 0.911377   | 4.198360   |
| Decision Tree | 4177 | FakeNews | 0.909918   | 8.145076   |
| Decision Tree | 4950 | Base     | 0.981566   | 9.747898   |
| Decision Tree | 8354 | FakeNews | 0.950764   | 16.745201  |
| Decision Tree | 9900 | Base     | 0.976768   | 20.956969  |
|               |      |          |            |            |
| Logistic      | 1980 | Base     | 0.995581   | 6.365607   |
| Logistic      | 2088 | FakeNews | 0.989820   | 3.731460   |
| Logistic      | 4177 | FakeNews | 0.996409   | 8.011122   |
| Logistic      | 4950 | Base     | 0.998990   | 10.535047  |
| Logistic      | 8354 | FakeNews | 0.997606   | 16.900789  |
| Logistic      | 9900 | Base     | 0.998737   | 20.922753  |



#### Next steps
What suggestions do you have for next steps?

#### Outline of project

- [Link to notebook 1]()
- [Link to notebook 2]()
- [Link to notebook 3]()


##### Contact and Further Information