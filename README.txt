1) Dependency graphs
b. 
Below discusses how to determine if a sentence is projective.
We insert each arc (parent, child) into the dependency graph. After that, we force child index to be smaller than the parent index, since whether the dependency for this node is from child to parent or opposite does not matter for projectivity check.
Then, we run a for loop k for each index within the range of [child index+1, parent index-1], and within the loop we run an innner loop m for a length of len(depgraph.nodes), thus iterating over all nodes of the dependency graph.
In this inner loop, we check if m is before child index or after parent index, thus possible to produce a conflict with (child index, parent index). If this is the case, we check if k and m indeed exists in the dependency graph's arc list, and if so then there's a intersection between the two lines (k,m) and (child index, parent index) and so returns false (non-projective). 
Therefore, what we are  looking for is really just whether two dependency intersect/cross with each other, and if so then not projective.

c.
projective: I have a cat.
non-projective: I saw a flower yesterday that is pretty.

2)
UAS: 0.229038040231 
LAS: 0.125473013344
The performance for badfeatures.model is really bad, so we have to select better features for better performance.

3)
English: 
UAS: 0.808176100629
LAS: 0.770440251572

Swedish:
UAS: 0.785899223262 
LAS: 0.675960963951

Danish:
UAS: 0.797604790419
LAS: 0.717365269461

Features:
0) word, lemma, ctag, tag, feats, ldep, rdep of top word on stack (stack[-1]), O(1), improves performance a lot(some in this category is originally included in provided code already)
1) Tag of stack[-2]. i.e. the pos tag of the word second on the top of the stack, O(n), improves performance a lot

6) word, lemma, ctag, tag, feats, ldep, rdep of top word on buffer (buffer[0]), O(1), improves performance a lot(some in this category is originally included in provided code already)
13) Word, ctag, tag of buffer[1]. i.e. the pos tag of the word second on the top of the buffer, O(1), improves performance a lot
14) Ctag, tag of buffer[2], O(1), improves performance by a bit
15) Tag of buffer[3], O(1), improves performance by a bit
16) STK_0_BUF_0_DIS: Distance between the top stack word and top buffer word (length between stack[-1] and buffer[0]), O(1), improves performance by a little


Complexity of arc-eager shift-reduce parser: 
The parsing algorithm is based on shift-and-reduce, while adding right and left arc to process dependency relationships in the sentence. At testing time, classifier determines the next action by having a outer single pass over the sentence. The algorithm itself is O(n), since the process is linear and the program never looks back, with n being the length of the sentence.
However, because of the features it's a bit more than that. For each sentence, it looks at features 0,1,6,13,14,15,16 which are all O(1) so they have no effect.

So total complexity is O(n)*O(1) = O(n).

Trade-offs: Since the parser only looks at each sentence exactly once, it's not able to parse the non-projective sentences' dependency. Also, accuracy (number and quality of features it looks at) trades off with time. The more and more elaborate and informative the deatures (that requires search), the slower it becomes.
Also, the algorithm needs enough training data in order to behave well. Furthermore, since the features are manually selected, the selection should be good enough as well.















