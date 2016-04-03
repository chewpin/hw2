class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        # print "before, ", conf.__str__()
        if not conf.stack or not conf.buffer:
            # print "LEFT ARC stack or buffer empty: -1", conf.__str__()
            return -1
        w_i = conf.stack[-1]
        w_j = conf.buffer[0]
        if w_i == 0:
            # print "LEFT ARC ", w_i, " == ROOT: -1", conf.__str__()
            return -1
        for arc in conf.arcs:
            if arc[2] == w_i:
                # print "LEFT ARC ", w_i, " in arcs[1]: -1", conf.__str__()
                return -1
        del conf.stack[-1]
        conf.arcs.append( (w_j, relation, w_i))


        # print "after, ", conf.__str__()
        # raise NotImplementedError('Please implement left_arc!')
        # return -1

    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        # print "before, ", conf.__str__()
        if not conf.buffer or not conf.stack:
            # print "RIGHT ARC buffer or stack empty: -1", conf.__str__()
            return -1

        # You get this one for free! Use it as an example.

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        conf.stack.append(idx_wj)
        conf.arcs.append((idx_wi, relation, idx_wj))
        # print "after, ", conf.__str__()

    @staticmethod
    def reduce(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        precond_met = False
        # print "before, ", conf.__str__()
        if not conf.stack or not conf.arcs:
            # print "REDUCE stack or arcs empty: -1", conf.__str__()
            return -1
        w_i = conf.stack[-1]
        for arc in conf.arcs:
            if arc[2] == w_i:
                precond_met = True
                break
        if not precond_met:
            # print "REDUCE ", w_i, " not in arcs[1]: -1", conf.__str__()
            return -1
        del conf.stack[-1]
        # print "after, ", conf.__str__()
        # raise NotImplementedError('Please implement reduce!')
        # return -1

    @staticmethod
    def shift(conf):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        # print "before, ", conf.__str__()
        if not conf.buffer:
            print "\n\n\nshift buffer empty: -1", conf.__str__()
            return -1
        conf.stack.append(conf.buffer.pop(0))
         
        # print "after, ", conf.__str__()
        # raise NotImplementedError('Please implement shift!')
        # return -1









