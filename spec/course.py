'''
Course website specifications
'''

from .err import Feat, Req
from .exercise_superspec import TabbedExercise

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

class SectionRomanExamples(Req):
    """
    Section 1.5 must present Lean 4 formalization exercises for the examples in Steven Roman's lecture.
    """

class ExerciseGroupInverseUnique(TabbedExercise):
    """
    Lean 4 exercise proving that inverses in a group are unique.
    Uses a calc block to chain equalities via left/right cancellation.
    Both tabs required: sorry stub and a complete calc proof.
    """
    title = "Group Inverse Uniqueness"
    section = "1.5"
    difficulty = "beginner"
    sorry_code = (
        "import Mathlib\n"
        "theorem inv_unique {G : Type*} [Group G] (a b : G)\n"
        "    (hl : a * b = 1) : b = a⁻¹ := by\n"
        "  sorry\n"
    )
    solution_code = (
        "import Mathlib\n"
        "theorem inv_unique {G : Type*} [Group G] (a b : G)\n"
        "    (hl : a * b = 1) : b = a⁻¹ := by\n"
        "  calc b = 1 * b         := by ring\n"
        "       _ = (a⁻¹ * a) * b := by simp\n"
        "       _ = a⁻¹ * (a * b) := by ring\n"
        "       _ = a⁻¹ * 1       := by rw [hl]\n"
        "       _ = a⁻¹            := by ring\n"
    )


class ExercisePosetAsCategory(TabbedExercise):
    """
    Lean 4 exercise showing that any preorder (Preorder α) gives rise to a
    category whose objects are elements of α and whose hom-sets are
    Props (at most one morphism between any two objects).
    Both tabs required: sorry stub and a complete Category instance.
    """
    title = "Poset as a Category"
    section = "1.5"
    difficulty = "beginner"
    sorry_code = (
        "import Mathlib\n"
        "universe u\n"
        "variable {α : Type u} [Preorder α]\n"
        "-- Provide the Category instance for a preorder.\n"
        "instance posetCategory : CategoryTheory.SmallCategory α where\n"
        "  Hom a b := PLift (a ≤ b)\n"
        "  id a    := sorry\n"
        "  comp f g := sorry\n"
    )
    solution_code = (
        "import Mathlib\n"
        "universe u\n"
        "variable {α : Type u} [Preorder α]\n"
        "instance posetCategory : CategoryTheory.SmallCategory α where\n"
        "  Hom a b   := PLift (a ≤ b)\n"
        "  id a      := ⟨le_refl a⟩\n"
        "  comp f g  := ⟨le_trans f.down g.down⟩\n"
    )


class ExerciseMonoidAsCategory(TabbedExercise):
    """
    Lean 4 exercise defining a monoid as a single-object category:
    objects = Unit, morphisms = the monoid elements, composition = mul.
    Both tabs required: sorry stub and a complete Category instance.
    """
    title = "Monoid as a Single-Object Category"
    section = "1.5"
    difficulty = "intermediate"
    sorry_code = (
        "import Mathlib\n"
        "variable (M : Type*) [Monoid M]\n"
        "-- Define the single-object category whose morphisms are M.\n"
        "instance monoidCategory : CategoryTheory.Category Unit where\n"
        "  Hom _ _ := M\n"
        "  id  _   := sorry\n"
        "  comp f g := sorry\n"
    )
    solution_code = (
        "import Mathlib\n"
        "variable (M : Type*) [Monoid M]\n"
        "instance monoidCategory : CategoryTheory.Category Unit where\n"
        "  Hom _ _  := M\n"
        "  id  _    := (1 : M)\n"
        "  comp f g := f * g\n"
        "  id_comp  := one_mul\n"
        "  comp_id  := mul_one\n"
        "  assoc    := mul_assoc\n"
    )


class ExerciseMatrixCategory(TabbedExercise):
    """
    Lean 4 exercise defining the category of matrices over a commutative ring:
    objects = ℕ (dimensions), morphisms n ⟶ m = Matrix (Fin m) (Fin n) R,
    composition = matrix multiplication.
    Both tabs required: sorry stub and a complete Category instance.
    """
    title = "Category of Matrices"
    section = "1.5"
    difficulty = "intermediate"
    sorry_code = (
        "import Mathlib\n"
        "variable (R : Type*) [CommRing R]\n"
        "instance matrixCategory : CategoryTheory.Category ℕ where\n"
        "  Hom n m  := Matrix (Fin m) (Fin n) R\n"
        "  id  n    := sorry\n"
        "  comp f g := sorry\n"
    )
    solution_code = (
        "import Mathlib\n"
        "variable (R : Type*) [CommRing R]\n"
        "instance matrixCategory : CategoryTheory.Category ℕ where\n"
        "  Hom n m  := Matrix (Fin m) (Fin n) R\n"
        "  id  n    := 1                    -- identity matrix\n"
        "  comp f g := f * g                -- matrix multiplication\n"
        "  id_comp  := Matrix.one_mul\n"
        "  comp_id  := Matrix.mul_one\n"
        "  assoc    := Matrix.mul_assoc\n"
    )


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

