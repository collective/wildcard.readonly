import transaction
from zope.component import adapter
try:
    # Attempt to import ZPublisherEventsBackport to support older zopes
    # must come before imports from ZPublisher.interfaces
    import ZPublisherEventsBackport
except ImportError:
    pass
from ZPublisher.interfaces import IPubBeforeCommit
from ZPublisher.interfaces import IPubAfterTraversal
import logging
logger = logging.getLogger('hardenedplone')


@adapter(IPubAfterTraversal)
def readOnlyAllDoom(event):
    transaction.abort()

@adapter(IPubBeforeCommit)
def readOnlyAll(event):
    transaction.abort()

@adapter(IPubBeforeCommit)
def readOnlyRequest(event):
    req = event.request
    if req.get_header('X-Doom-Transaction'):
        transaction.abort()

@adapter(IPubBeforeCommit)
def readOnlyIfCommit(event):
    req = event.request
    app = req.PARENTS[-1]
    if len(app._p_jar._registered_objects) > 0:
        # check if there are any registered objects.
        # If there are, abort the transaction as that
        # means data is about to be committed to the database.
        logger.info('aborted committing to database')
        transaction.abort()
