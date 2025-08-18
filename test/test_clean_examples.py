from unittest import TestCase

from unstructured.partition.pdf import partition_pdf

from src.clean_examples import clean_text


class Test(TestCase):
    def test_clean_text(self):
        expected = "UNSTRUCTURED: Cleaning Test  Page ONE This document is deliberately MESSY. Itcontains extra spaces, tabs, and inconsistent casing. Email: TEST _User+spam@Example.com _ url: HTTP://EXAMPLE.com/Path?Q=1. Headings? maybe.  Section A  Some sentences... have odd punctuation !!! And wrongdashusage  like this. Line break hyphenation ex  ample should be merged across lines. Also multiple spaces should become one. Smart quotes: curly and single vs \"straight\" quotes. Non breaking spaces here. Unicode oddities: caf, naive, codperate, emoji: J]  ensure normalization (NFC). Page 1  Generated 2025 08 18 20:25:01 /// Contact: Example Co. Lists, Markup & Fragments (p.2) Shopping list (messy bullets): * apples   Bananas * oranges 1) milk 2.) bread 3. eggs Markdown ish: ### Title??? > A blockquote that may or may not be real. inline code and ~~ multiline code block ~*~ HTML snippet: <div class=\"note\"> <p> Hello <b>world</b>! </p> <ul><li> one </li> <li> two </li></ul></div> Random caps and spacing: This Is a TeST Of NorMALIZation. Odd punctuation spacing :like this ,and this .And this !? Page 2  Generated 2025 08 18 20:25:02 /// Contact: Example Co. Numbers, Dates & Entities (03) Dates (varied): 2025 08 18; 18/08/2025; Aug 18th, 2025; Monday 18th of August, '25. Currencies: $1,234.50;  999 , 95 ; 0.99 ; JPY 1 000 ; INR21000 ; CHF 1'234.56. Phone: +1 (415) 555  1234 ; +49 30  123456 ; (020) 7946 0018. OCR ish artifacts: The quick brown fOx jumps Over the lazy dOg. rn and m can look similar: mod ern  > modern. Broken words at end of line should be de  hyphenated where appropriate; BUT re  spect true hyphenated terms like state of the art. Weird control chars: form feed here; and a tab there; and non breaking spaces. Page 3  Generated 2025 08 18 20:25:02 /// Contact: Example Co. Simulated Table & Misc (IV) CSV ish table (ragged): id, name, amount, date 1, Alice, 12.00 ,2025/01/02 2 ,Bob, 7.5, 2025 1 3 003, \"Carol D.\", 1000, 18 08 2025 URLs & tracking params: https://example.com/search?q=cleaning https://example.com/article?utm_source=Email&utm_medium=CAMPAIGN&utm_campaign=Summer mailto: support@example.org , dev+ops@example.org Misc:  em dashes    en dashes     hyphens   doubled dashes Multiple = blank lines follow: END OF TEST DOCUMENT. Page 4  Generated 2025 08 18 20:25:02 /// Contact: Example Co"
        elements = partition_pdf("../files/unstructured-text.pdf")
        raw_text = "\n".join(str(e) for e in elements)
        cleaned_text = clean_text(raw_text)
        assert cleaned_text == expected
