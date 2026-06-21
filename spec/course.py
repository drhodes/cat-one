'''
Course website specifications
'''

from .err import Feat, Req

class CourseSite(Feat):
    """
    The online course is a premium, responsive static website.
    It serves as a Masterclass for Category Theory for Programmers using Lean 4 & Mathlib.
    """

class SectionPhilosophicalMotivation(Req):
    """
    Section 1 must introduce the core philosophy and motivation behind category theory.
    It must include:
    - Lecture 1: "Motivation and Philosophy" by Bartosz Milewski (Video ID: I8LbkfSSR58).
    - Lecture 2: "Intro to Category Theory 1" by Steven Roman (Video ID: If6VUXZIB-4).
    """

class SectionCategoriesObjectsMorphisms(Req):
    """
    Section 2 must define categories, objects, and morphisms.
    It must include:
    - Lecture 3: "What is a Category?" by Bartosz Milewski (Video ID: p54Hd7AmVFU).
    - Lecture 4: "Definition of a Category" by Martin Codrington (Video ID: 80bbALpA8k8).
    - A Lean 4 exercise defining category structure and proving identity composition.
    """

class SectionCategoryOfTypes(Req):
    """
    Section 3 must introduce the category of types.
    It must include:
    - Lecture 5: "Category of Sets/Types" by Richard Southwell (Video ID: US4Zr1WKD-8).
    - Lecture 6: "Isomorphisms" by Richard Borcherds (Video ID: JOp7mH72Jlg).
    - A Lean 4 exercise proving function composition associativity.
    """

class SectionEpimorphismsMonomorphisms(Req):
    """
    Section 4 must define epimorphisms and monomorphisms.
    It must include:
    - Lecture 7: "Epimorphisms" by Bartosz Milewski (Video ID: O2lZkr-aAqk).
    - Lecture 8: "Groupoids" (Video ID: YcyG8v1TcZ8).
    - A Lean 4 exercise showing epi cancellation.
    """

class SectionUniversalProperties(Req):
    """
    Section 5 must define products and coproducts using universal properties.
    It must include:
    - Lecture 9: "Duality and Universal Properties" by Richard Southwell (Video ID: oIc0K81yz6E).
    - Lecture 10: "Products" by Steve Awodey (Video ID: 2XReBRzOBWU).
    - A Lean 4 exercise constructing unique product morphisms.
    """

class SectionFunctors(Req):
    """
    Section 6 must introduce functors as structure-preserving mappings.
    It must include:
    - Lecture 11: "Functors and Slice Categories" by Steve Awodey (Video ID: ZKmodCApZwk).
    - Lecture 12: "Preserving Structure" (Video ID: Xz48SqxHx3w).
    - A Lean 4 exercise proving that map preserves composition.
    """

class SectionNaturalTransformations(Req):
    """
    Section 7 must define natural transformations and naturality squares.
    It must include:
    - Lecture 13: "Category Theory Foundations" by Steve Awodey (Video ID: 8fZmdhLLgs4).
    - Lecture 14: "Category Theory in Life" by Eugenia Cheng (Video ID: ho7oagHeqNc).
    - A Lean 4 exercise proving the naturality square.
    """

class SectionYonedaLemma(Req):
    """
    Section 8 must explain the Yoneda Lemma and representable functors.
    It must include:
    - Lecture 15: "The Yoneda Lemma" by Steve Awodey (Video ID: BOynNljjbeg).
    - Lecture 16: "Representable Functors" by Steve Awodey (Video ID: B6vmemDaPLc).
    """

class SectionAppliedCategoryTheory(Req):
    """
    Section 9 must introduce Applied Category Theory (ACT).
    It must include:
    - Lecture 17: "Generative Effects (Part 1)" by David Spivak (Video ID: UusLtx9fIjs).
    - Lecture 18: "Generative Effects (Part 2)" by Brendan Fong (Video ID: 2BYl7NgHjvc).
    """

class SectionFutureVerification(Req):
    """
    Section 10 must cover monoidal categories, resources, and the future of verification.
    It must include:
    - Lecture 19: "Resources and Monoidal Preorders" by David Spivak (Video ID: Cf3tsAeGhBg).
    - Lecture 20: "Category Theory (Lecture 1)" by Alex Simpson (Video ID: xwNG0R311q4).
    """

class MathJaxRendering(Req):
    """
    The site must load and initialize MathJax to render LaTeX equations cleanly.
    """

class ResponsiveDesign(Feat):
    """
    The layout must be responsive, modern, and visually stunning, featuring a video grid, clear tags, and dark-themed code highlights.
    """

class GitHubPagesHosting(Feat):
    """
    The course website must be deployable as a static site hosted on GitHub Pages.
    """

class MainBranchDeployment(Req):
    """
    The site must be served from the main branch of the repository, requiring all static assets to be directly accessible from the main branch.
    """

class RootEntrypoint(Req):
    """
    The primary entry point of the website must be an `index.html` file located in the root of the project to allow GitHub Pages to automatically serve it.
    """

