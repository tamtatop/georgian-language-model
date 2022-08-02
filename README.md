### Info
* Use `env.yml` to create identical conda env to us.
* Unfortunately, since we had a comfort of azure GPU instance we did not try to run these notebooks on 
google collab. If you run into problems you can message us and we'll give you access to our private
juputer-lab instance on azure.

Main notebooks:

* `no_en_data_prep.ipynb` - Remove all letters except georgian; filter data; separate sentences and split data 
in train, test, validation.
* `eda.ipynb` - EDA
* `w2v.ipynb` - word2vec training on cleaned data
* `word2vec_analysis.ipynb` - this analysis was done on a bigger/earlier w2v model(from geolm.ipynb). before we filtered out english
* `geolm.ipynb` - notebook for training next token prediction transformer (with or without w2v(old)).
	* we gave up on this model since it was not learning anything and loss was not decreasing
	* we didn't try any evaluation for this since it was hopeless. any sentece would only generate same tokens
* `v2bert-tokenizer-training.ipynb` - training subword tokenizer
* `subword-w2v.ipynb` - subword word2vec and it's simple analysis. subwording is done with tokenizer from above
* `bert-v2-train.ipynb` - notebook for training bert with or without word2vec
	* `bert-v1-train.ipynb` - historical training notebook for v1 bert (no w2v). trained for 10hr (no test data)
* `bert-textgen-eval.ipynb` - text generation and evaluation for bert models
	* `lm_demo.ipynb` - stripped down version of this

Training logs(loss):
v1 bert logs: `polished/models/bert/trainer/trainer_state_part1.json`
v2 bert with w2v: `./polished/models/v2bert/trainer/trainer_state.json`
v2 bert without w2v: `./polished/models/ka_only_no_w2v_bert/trainer/trainer_state.json`

Troubleshoot: 
`ka_nse_mil` in some notebooks can be replaced with any file from `./no_en_data/`. We are keeping it
like this for clean history
