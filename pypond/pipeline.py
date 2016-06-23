#  Copyright (c) 2016, The Regents of the University of California,
#  through Lawrence Berkeley National Laboratory (subject to receipt
#  of any required approvals from the U.S. Dept. of Energy).
#  All rights reserved.
#
#  This source code is licensed under the BSD-style license found in the
#  LICENSE file in the root directory of this source tree.

"""
Implementation of the Pond Pipeline classes.

http://software.es.net/pond/#/pipeline
"""

from .bases import PypondBase


class Runner(PypondBase):  # pylint: disable=too-few-public-methods
    """
    A runner is used to extract the chain of processing operations
    from a Pipeline given an Output. The idea here is to traverse
    back up the Pipeline(s) and build an execution chain.

    When the runner is started, events from the "in" are streamed
    into the execution chain and outputed into the "out".

    Rebuilding in this way enables us to handle connected pipelines:

    ::

                            |--
         in --> pipeline ---.
                            |----pipeline ---| -> out

    The runner breaks this into the following for execution:

    ::

          _input        - the "in" or from() bounded input of
                          the upstream pipeline
          _processChain - the process nodes in the pipelines
                          leading to the out
          _output       - the supplied output destination for
                          the batch process

    NOTE: There's no current way to merge multiple sources, though
          a time series has a TimeSeries.merge() static method for
          this purpose.

    Parameters
    ----------
    pipeline : Pipeline
        The pipeline to run.
    output : PipelineOut
        The output driving this runner
    """

    def __init__(self, pipeline, output):
        """Create a new batch runner"""
        super(Runner, self).__init__()

        self._pipeline = pipeline
        self._output = output

        # We use the pipeline's chain() function to walk the
        # DAG back up the tree to the "in" to:
        # 1) assemble a list of process nodes that feed into
        #    this pipeline, the processChain
        # 2) determine the _input
        #
        # NOTE: we do not currently support merging, so this is
        # a linear chain.

        # Using the list of nodes in the tree that will be involved in
        # our processing we can build an execution chain. This is the
        # chain of processor clones, linked together, for our specific
        # processing pipeline. We run this execution chain later by
        # evoking start().

    def start(self, force=False):
        """Start the runner

        Args:
            force (bool, optional): force Flush at the end of the batch source
            to cause any buffers to emit.
        """
        # Clear any results ready for the run

        # The head is the first process node in the execution chain.
        # To process the source through the execution chain we add
        # each event from the input to the head.

        # The runner indicates that it is finished with the bounded
        # data by sending a flush() call down the chain. If force is
        # set to false (the default) this is never called.
        pass


class Pipeline(PypondBase):
    """
    Build a new Pipeline.

    A pipeline manages a processing chain, for either batch or stream processing
    of collection data.

    The argument may be either:

    - a Pipeline (copy ctor)
    - a pyrsistent.PMap in which case the internal state will be constructed from the map.

    Usually you would initialize a Pipeline using the factory function,
    rather than this object directly.

    Parameters
    ----------
    arg : Pipeline, PMap, None
        See above.

    Returns
    -------
    TYPE
        Description
    """

    def __init__(self, arg):
        """New pipeline."""
        super(Pipeline, self).__init__()








































