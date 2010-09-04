from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from acentoweb.insurance import _

YesNoVocabulary = SimpleVocabulary(
    [SimpleTerm(value='yes', title=_(u'Yes')),
     SimpleTerm(value='no', title=_(u'No'))],
    )
