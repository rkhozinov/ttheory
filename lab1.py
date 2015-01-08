#!/usr/bin/python2
import sys
import math


def stream_load(stream_performace, streams_num, free_stream_probability):
    return (stream_performace ** streams_num) / math.factorial(streams_num) * free_stream_probability


def lab1(args):
    stream_num = int(args[0])

    orders = int(args[1])
    working_time = int(args[2])
    average_order_time = int(args[3])

    print stream_num
    print orders
    print working_time
    print average_order_time

    stream_performance = working_time / average_order_time
    print ("1. stream performance: {} orders".format(stream_performance))

    order_process_time = float(average_order_time) / working_time
    print ("   processing time of the one order: {} min".format(order_process_time))

    common_loading = orders * average_order_time / working_time
    print ("2. common loading: {}".format(common_loading))

    stream_free_probability = stream_performance / float(orders + stream_performance)
    print ("3. the stream will be free {}% of working time".format(int(stream_free_probability * 100)))

    stream_free_time = int(working_time * stream_free_probability)
    print ("   non working time of the stream is {} min".format(stream_free_time))

    stream_loading = stream_load(common_loading, stream_num, stream_free_probability)
    print ("   loading of the stream: {}".format(stream_loading))

    stream_denied_of_service = stream_loading
    print ("4. denied probability of the stream: {}".format(stream_denied_of_service))

    stream_rel_bandwitdh = 1 - stream_denied_of_service
    print ("5. {}% orders will be served".format(stream_rel_bandwitdh * 100))

    stream_abs_bandwitdh = stream_rel_bandwitdh * orders
    print ("   speed of service: {} orders per {} min".format(stream_abs_bandwitdh, working_time))

    average_working_streams = common_loading * stream_rel_bandwitdh
    print ("6. average of working streams {}".format(average_working_streams))

    average_free_streams = 1 - average_working_streams

    print ("   average of free streams {}".format(average_free_streams))

    loading_of_streams = average_working_streams / stream_num
    print ("7. loading of streams {}".format(loading_of_streams))

    average_free_time_of_stream = stream_denied_of_service * order_process_time
    print ("8. average free time of the stream: {}".format(average_free_time_of_stream))

    average_of_processed_orders = common_loading * stream_rel_bandwitdh
    print ("9. average of processed orders: {}".format(average_of_processed_orders))

    denied_orders = orders * common_loading
    print ("10.denied orders: {}".format(denied_orders))

    abs_performance = 1 / order_process_time
    print ("11.absolute performance: {}".format(abs_performance))

    real_performance = stream_abs_bandwitdh / abs_performance
    print ("   real performance: {}%".format(real_performance * 100))


if __name__ == "__main__":
    lab1(sys.argv[1:])
