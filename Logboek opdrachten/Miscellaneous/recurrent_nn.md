### Recurrent Neural Networks
A recurrent neural network is a type of neural network which is specialized in processing sequential or temporal data. 
They are a popular choice for many problems such as  language translation, natural language processing and speech 
recognition.

![A basic feed-forward neural network](https://lh4.googleusercontent.com/FQ_odF4g2X2Dn3wInyyK8bG1SHY8QuAyOUIdl_cGcuHkKWMiiFhu2RtKd-hH8RnAsR_yO12Vc0Wru_O5t89rqVMt8fJcrHOZGASYD3W3lOqVJmRhKIQXQFJZJ5bpE2XxTcJOc6bC)
*A basic feed-forward neural network*

In our text classification problem there are some problems with a traditional feed-forward neural network. Take for 
example the sentence “our service maid paid no attention to cleaning”. With this network each of those words would 
get processed separately from each other, which means we can lose context. “Service”, “ attention”  and “ cleaning”  
are all positive if you look at them one by one, with the meaning only changing once you assemble the total structure 
of the sentence, which totally flips the sentiment. And if “no” is the only negative word in the sentence, the model 
could throw preference to predicting the sentence as positive, while all humans could see otherwise.



![A basic recurrent neural network](https://lh4.googleusercontent.com/1dKbnO_4SeMhGN-0QEPdrE8k0HETM2DOMtvLsGT0oHSS3Dc8RH2NfYhIQGGk6gHiJ5YfJ-adiLrycoY3XuR3Ngc72AKlTM9yC5ku2PdnNC5stTytKjiQIxgjhqiP1j4tg4C2KWpC)
*A basic recurrent neural network* 

There are several ways to solve this problem, and a recurrent neural network, commonly abbreviated as RNN is one of them. 
A RNN solves this by essentially having its own “memory”. Each neuron can receive information from the previous neuron, 
and thus build up a short term memory of the current sequence. See below image for a good example of how this can look 
like.

![A rolled vs unrolled RNN](https://lh4.googleusercontent.com/f6i21vjFgNKYF1xUGqK9Ks3faa3z5gvobAXkWDNPPIG6a91BmV-5ZrRIxPSLvKfPx4nJcR07u4ovqnGO5A_LDVxh36bN2SoyBPF-YYMvqPn6Rjr-ofiBO0LfDVEKEaJCycZWCYDj)
*A rolled vs unrolled RNN*

### LSTM & GRU
This short-term memory has a problem though, where the name says it all, it can’t remember things in the long term. 
This is due to something called the vanishing gradient problem. During back propagation our neural network adjusts 
the values in our network, adjusting their numbers. A simplified explanation of the vanishing gradient is that 
these number updates become so small that our model essentially stops learning. In the context of our problem, 
this would mean that our RNN is fine with short sentences but will massively struggle if someone posts long paragraphs.

Both LSTM (Long Short Term Memory) and GRU (Gated Recurrent Unit) were introduced to solve this problem.

![Internal view of LSTM and GRU](https://lh3.googleusercontent.com/2EpAqUvtRFr6suN7VGoHofkdlUfvqT3h7Hys3sGqzv-6o-6qv7HObGDMt1y3njq1sjVZHs07QKufwh7gdCtGlxOQRg9VDEC8PzM-UjjTZGYDoRK9lfCr8LtQC5i3AbXti2sSb_Qs)
*Internal view of LSTM and GRU* 

These units work on a concept called gates. These are internal mechanisms inside a neuron that make a decision on what 
information to forget, what to add and what to give to the next neuron. This is in contrast to a basic RNN which only 
performs a basic mathematical function on the input and then passes it along to the next neuron.

So what is the difference between them? For one, they have a different internal structure. GRU is about a decade newer, 
having been first proposed in 2014, compared to LSTM’s 1997. In practice though it seems that they perform rather 
similarly, with GRU perhaps having a slight edge performance wise. (Chung et al., Empirical Evaluation of 
Gated Recurrent Neural Networks on Sequence Modeling) I couldn’t find a source on a comparison between performance 
metrics, which tells me that which one you select is probably on a per-preference basis.
