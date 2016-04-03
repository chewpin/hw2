from nltk.compat import python_2_unicode_compatible
import nltk
printed = False

@python_2_unicode_compatible
class FeatureExtractor(object):
    @staticmethod
    def _check_informative(feat, underscore_is_informative=False):
        """
        Check whether a feature is informative
        """

        if feat is None:
            return False

        if feat == '':
            return False

        if not underscore_is_informative and feat == '_':
            return False

        return True

    @staticmethod
    def find_left_right_dependencies(idx, arcs):
        left_most = 1000000
        right_most = -1
        dep_left_most = ''
        dep_right_most = ''
        for (wi, r, wj) in arcs:
            if wi == idx:
                if (wj > wi) and (wj > right_most):
                    right_most = wj
                    dep_right_most = r
                if (wj < wi) and (wj < left_most):
                    left_most = wj
                    dep_left_most = r
        return dep_left_most, dep_right_most

    @staticmethod
    def extract_features(tokens, buffer, stack, arcs):
        """
        This function returns a list of string features for the classifier

        :param tokens: nodes in the dependency graph
        :param stack: partially processed words
        :param buffer: remaining input words
        :param arcs: partially built dependency tree

        :return: list(str)
        """

        """
        Think of some of your own features here! Some standard features are
        described in Table 3.2 on page 31 of Dependency Parsing by Kubler,
        McDonald, and Nivre

        [http://books.google.com/books/about/Dependency_Parsing.html?id=k3iiup7HB9UC]
        """

        result = []


        global printed
        if not printed:
            # print("This is not a very good feature extractor!")
            printed = True

        # an example set of features:
        if stack:
            stack_idx0 = stack[-1]
            token = tokens[stack_idx0]
            if FeatureExtractor._check_informative(token['word'], True):
                result.append('STK_0_FORM_' + token['word'])
            if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
                lemma = token['lemma']
                result.append('STK_0_NEW_LEMMA_' + lemma)
            if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
                ctag = token['ctag']
                # result.append('STK_0_NEW_CTAG_' + ctag)
                result.append("STK_0_NEW_CTAG_" + nltk.tag.mapping.map_tag("en-ptb", "universal", ctag))
            if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
                tag = token['tag']
                result.append('STK_0_NEW_TAG_' + tag)
            if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
                feats = token['feats'].split("|")
                for feat in feats:
                    result.append('STK_0_FEATS_' + feat)

            # Left most, right most dependency of stack[0]
            dep_left_most, dep_right_most = FeatureExtractor.find_left_right_dependencies(stack_idx0, arcs)

            if FeatureExtractor._check_informative(dep_left_most):
                result.append('STK_0_LDEP_' + dep_left_most)
            if FeatureExtractor._check_informative(dep_right_most):
                result.append('STK_0_RDEP_' + dep_right_most)
            if len(stack) > 1:
                stack_idx1 = stack[-2]
                token = tokens[stack_idx1]
                if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
                    tag = token['tag']
                    result.append('STK_1_NEW_TAG_' + tag)




            # find which depends on STK_0 
            # left_children_num = right_children_num = 0
            # STK_0_CHILD_dict = set()
            # for arc in arcs:
            #     if arc[0] == stack_idx0:
            #         if stack_idx0 < arc[2]:
            #             right_children_num += 1
            #         else:
            #             left_children_num += 1
            #         other_token = tokens[arc[2]]
            #         if FeatureExtractor._check_informative(token['word'], True):
            #             if 'STK_0_CHILD_' + token['word'] not in STK_0_CHILD_dict:
            #                 STK_0_CHILD_dict.add('STK_0_CHILD_' + token['word'])
                            # result.append('STK_0_CHILD_' + token['word'])
            # result.append('STK_0_LEFT_CHILD_NUM_' + str(left_children_num))
            # result.append('STK_0_RIGHT_CHILD_NUM_' + str(right_children_num))

            # find which STK_0 depends on # improves a tiny bit
            # left_parent_num = right_parent_num = 0
            # STK_0_PARENT_dict = set()
            # for arc in arcs:
            #     if arc[2] == stack_idx0:
            #         if stack_idx0 < arc[0]:
            #             right_parent_num += 1
            #         else:
            #             left_parent_num += 1
            #         other_token = tokens[arc[0]]
            #         if FeatureExtractor._check_informative(token['word'], True):
            #             if 'STK_0_PARENT_' + token['word'] not in STK_0_PARENT_dict:
            #                 STK_0_PARENT_dict.add('STK_0_PARENT_' + token['word'])
                            # result.append('STK_0_PARENT_' + token['word'])
          #  # result.append('STK_0_LEFT_PARENT_NUM_' + str(left_parent_num))
          #  # result.append('STK_0_RIGHT_PARENT_NUM_' + str(right_parent_num))
        if buffer:
            buffer_idx0 = buffer[0]
            token = tokens[buffer_idx0]
            if FeatureExtractor._check_informative(token['word'], True):
                result.append('BUF_0_FORM_' + token['word'])
            if 'lemma' in token and FeatureExtractor._check_informative(token['lemma']):
                lemma = token['lemma']
                result.append('BUF_0_NEW_LEMMA_' + lemma)
            if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
                ctag = token['ctag']
                # result.append('BUF_0_NEW_CTAG_' + ctag)
                result.append("BUF_0_NEW_CTAG_" + nltk.tag.mapping.map_tag("en-ptb", "universal", ctag))
            if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
                tag = token['tag']
                result.append('BUF_0_NEW_TAG_' + tag)
            if 'feats' in token and FeatureExtractor._check_informative(token['feats']):
                feats = token['feats'].split("|")
                for feat in feats:
                    result.append('BUF_0_FEATS_' + feat)

            dep_left_most, dep_right_most = FeatureExtractor.find_left_right_dependencies(buffer_idx0, arcs)

            if FeatureExtractor._check_informative(dep_left_most):
                result.append('BUF_0_LDEP_' + dep_left_most)
            if FeatureExtractor._check_informative(dep_right_most):
                result.append('BUF_0_RDEP_' + dep_right_most)

            # left_children_num = right_children_num = 0
            # BUF_0_CHILD_dict = set()
            # for arc in arcs:
            #     if arc[0] == buffer_idx0:
            #         if buffer_idx0 < arc[2]:
            #             right_children_num += 1
            #         else:
            #             left_children_num += 1
            #         other_token = tokens[arc[2]]
            #         if FeatureExtractor._check_informative(token['word'], True):
            #             if 'BUF_0_CHILD_' + token['word'] not in BUF_0_CHILD_dict:
            #                 BUF_0_CHILD_dict.add('BUF_0_CHILD_' + token['word'])
                            # result.append('BUF_0_CHILD_' + token['word'])
            # result.append('BUF_0_LEFT_CHILD_NUM_' + str(left_children_num))
            # result.append('BUF_0_RIGHT_CHILD_NUM_' + str(right_children_num))
            # left_parent_num = right_parent_num = 0
            # BUF_0_PARENT_dict = set()
            # for arc in arcs:
            #     if arc[2] == buffer_idx0:
            #         if buffer_idx0 < arc[0]:
            #             right_parent_num += 1
            #         else:
            #             left_parent_num += 1
            #         other_token = tokens[arc[0]]
            #         if FeatureExtractor._check_informative(token['word'], True):
            #             if 'BUF_0_PARENT_' + token['word'] not in BUF_0_PARENT_dict:
            #                 BUF_0_PARENT_dict.add('BUF_0_PARENT_' + token['word'])
                            # result.append('BUF_0_PARENT_' + token['word'])
            # result.append('BUF_0_LEFT_PARENT_NUM_' + str(left_parent_num))
            # result.append('BUF_0_RIGHT_PARENT_NUM_' + str(right_parent_num))

            if len(buffer) > 1:
                buffer_idx1 = buffer[1]
                token = tokens[buffer_idx1]
                if FeatureExtractor._check_informative(token['word'], True):
                    result.append('BUF_1_FORM_' + token['word'])
                if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
                    tag = token['tag']
                    result.append('BUF_1_NEW_TAG_' + tag)
                if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
                    ctag = token['ctag']
                    result.append("BUF_1_NEW_CTAG_" + nltk.tag.mapping.map_tag("en-ptb", "universal", ctag))
                    # result.append('BUF_1_NEW_CTAG_' + ctag)

                if len(buffer) > 2:
                    buffer_idx2 = buffer[2]
                    token = tokens[buffer_idx2]
                    if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
                        tag = token['tag']
                        result.append('BUF_2_NEW_TAG_' + tag)
                    if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
                        ctag = token['ctag']
                        result.append("BUF_2_NEW_CTAG_" + nltk.tag.mapping.map_tag("en-ptb", "universal", ctag))
                        # result.append('BUF_2_NEW_CTAG_' + ctag)
                    if len(buffer) > 3:
                        buffer_idx3 = buffer[3]
                        token = tokens[buffer_idx3]
                        if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
                            tag = token['tag']
                            result.append('BUF_3_NEW_TAG_' + tag)
                        # if 'ctag' in token and FeatureExtractor._check_informative(token['ctag']):
                        #     ctag = token['ctag']
                        #     result.append('BUF_3_NEW_CTAG_' + ctag)
        if stack and buffer:
            intervene_words = set()
            stack_idx0 = stack[-1]
            buffer_idx0 = buffer[0]
            length = stack_idx0 - buffer_idx0
            if length < 0:
                length = -1 * length
            if stack_idx0 < buffer_idx0:
                start = stack_idx0
                end = buffer_idx0
            else:
                start = buffer_idx0
                end = stack_idx0
            n_return_length = 0
            v_return_length = 0
            if length > 1:
                for i in range(start+1,end):
                    token = tokens[i]
                    if FeatureExtractor._check_informative(token['word'], True):
                        if token['word'] not in intervene_words:
                            intervene_words.add(token['word'])
                    if 'tag' in token and FeatureExtractor._check_informative(token['tag']):
                        tag = token['tag']
                        if tag.lower()[0] == "v":
                            v_return_length += 1
                        if tag.lower()[0] == "n":
                            n_return_length += 1
            return_length = length
            # for word in intervene_words:
            #     result.append('STK_0_BUF_0_INTERVENE_' + word)

            result.append('STK_0_BUF_0_DIS_' + str(return_length))
            # result.append('STK_0_BUF_0_NDIS_' + str(n_return_length))
            # result.append('STK_0_BUF_0_VDIS_' + str(v_return_length))
        # arc_length_dict = {}
        # if arcs:
        #     for arc in arcs:
        #         length = arc[0] - arc[2]
        #         if length < 0:
        #             length = -1 * length
        #         if length in arc_length_dict:
        #             arc_length_dict[length] += 1
        #         else:
        #             arc_length_dict[length] = 1
        # for arc in arc_length_dict:
        #     result.append('ARC_LENGTH_' + str(arc) + "_" + str(arc_length_dict[arc]))
        #     result.append('ARC_LENGTH_' + str(arc))

        # print result
        return result







