"""
Exercise SuperSpec
==================
A standalone specification that defines the structural contract all Lean 4
exercises on the course page must satisfy.

**Deliberately excluded from main_spec.py / the module registry.**
This file exists solely as a normative superclass to be inherited by
individual exercise specs when those specs are written.  It is never
imported at the registry level so that it does not pollute the top-level
spec graph.

Usage
-----
In a per-exercise spec file (which may itself be excluded from the registry,
or included — author's choice), inherit from the classes here:

    from spec.exercise_superspec import TabbedExercise

    class MyGroupInverseExercise(TabbedExercise):
        \"\"\"Proves that group inverses are unique.\"\"\"
"""

from libspec import Ctx, Feature, Requirement


# ---------------------------------------------------------------------------
# Primitive contexts (self-contained; does not import from err.py so this file
# remains fully independent of the main spec graph)
# ---------------------------------------------------------------------------

class _Err(Ctx):
    """
    Error handling must be excellent.  Any failure in rendering or loading an
    exercise should surface a clear, human-readable message rather than
    silently showing a blank pane.
    """


class _Robustness(_Err):
    """
    Exercises must degrade gracefully: if MathJax or syntax highlighting fails
    to load, the raw Lean 4 source must still be legible.
    """


class _Refactor(Ctx):
    """
    Exercise rendering logic must live in a single, shared helper — not
    duplicated per-exercise.  Each exercise only supplies its metadata and two
    code strings (sorry body, solution body).
    """


# ---------------------------------------------------------------------------
# Tab structure requirements
# ---------------------------------------------------------------------------

class TwoTabStructure(Requirement, _Robustness):
    """
    Every exercise block rendered on the course page MUST contain exactly two
    tabs presented side-by-side (or via a toggle):

    Tab 1 — "Exercise"
        The Lean 4 theorem statement is shown in full.  The proof body is
        replaced by a single ``sorry`` so the reader sees a well-typed but
        unproved stub.  No partial hints may leak into this tab.

    Tab 2 — "Solution"
        The complete, compilable Lean 4 proof is shown verbatim.  The tab is
        labelled "Solution" and is visually distinct (e.g. a different accent
        colour or lock icon) so readers can resist peeking.

    Both tabs must be present and non-empty.  A missing tab is a spec
    violation.
    """


class SorryTabRequirement(Requirement, _Robustness):
    """
    The "Exercise" tab must satisfy all of the following:

    - The theorem or definition header (``theorem``, ``def``, ``instance``,
      etc.) appears unchanged from the solution, so the type signature is
      fully visible.
    - The proof body (everything between ``:= by`` / ``:=`` and the closing
      of the block) is replaced by the single keyword ``sorry``.
    - ``#check``, ``#eval``, or ``example`` statements that are purely
      demonstrative may be omitted or stubbed with ``sorry`` as appropriate.
    - The word ``sorry`` must not appear in the Solution tab.
    """


class SolutionTabRequirement(Requirement, _Robustness):
    """
    The "Solution" tab must satisfy all of the following:

    - The Lean 4 code is complete and must type-check against the current
      stable Mathlib version pinned in ``lakefile.toml``.
    - Import statements (e.g. ``import Mathlib``) appear at the top of the
      block if they are needed for context.
    - The proof is idiomatic: prefer ``simp``, ``ring``, ``omega``, ``exact``,
      ``calc``, and ``apply`` over raw term-mode proofs where readability is
      improved.
    - No ``sorry`` keyword appears anywhere in this tab.
    """


class TabAccessibility(Requirement, _Robustness):
    """
    The two-tab UI must be keyboard-navigable and screen-reader friendly:

    - Each tab button has a unique, descriptive ``id`` and an ``aria-controls``
      attribute pointing to its panel ``id``.
    - The active tab panel has ``aria-hidden="false"``; the inactive panel has
      ``aria-hidden="true"``.
    - Tab switching must not require JavaScript frameworks — vanilla JS only.
    """


class CodeHighlighting(Requirement, _Refactor):
    """
    Both tabs must apply syntax highlighting to the Lean 4 code blocks.
    The highlighting library (e.g. highlight.js or Prism) must be loaded
    once per page, not once per exercise.
    """


class ExerciseMetadata(Requirement, _Refactor):
    """
    Each exercise must expose the following metadata as attributes on its
    Python class (for potential future tooling, e.g. auto-generating a
    problem set PDF):

    ``title``        : str — human-readable exercise title
    ``section``      : str — section identifier (e.g. "1.5")
    ``difficulty``   : str — one of "beginner" | "intermediate" | "advanced"
    ``sorry_code``   : str — the Lean 4 stub (Exercise tab source)
    ``solution_code``: str — the complete Lean 4 proof (Solution tab source)
    """


# ---------------------------------------------------------------------------
# The superclass that exercise specs inherit
# ---------------------------------------------------------------------------

class TabbedExercise(
    TwoTabStructure,
    SorryTabRequirement,
    SolutionTabRequirement,
    TabAccessibility,
    CodeHighlighting,
    ExerciseMetadata,
    Feature,
    _Robustness,
    _Refactor,
):
    """
    Superclass for all Lean 4 exercises on the course page.

    Subclass this to define a concrete exercise spec.  The subclass docstring
    becomes the human-readable description of what the exercise must prove or
    construct.

    Inherited contracts (from the MRO):
    - Exactly two tabs: "Exercise" (sorry stub) and "Solution" (full proof).
    - Keyboard-accessible, ARIA-labelled tab UI.
    - Syntax highlighting via a single shared library instance.
    - Class-level metadata attributes for tooling integration.
    - Graceful degradation if JS or MathJax fails.

    Example subclass (kept out of the registry)::

        class ExerciseGroupInverse(TabbedExercise):
            \"\"\"
            Proves that left and right inverses in a group coincide,
            therefore inverses are unique.
            \"\"\"
            title = "Group Inverse Uniqueness"
            section = "1.5"
            difficulty = "beginner"

            sorry_code = '''
    theorem inv_unique {G : Type*} [Group G] (a b : G)
        (h : a * b = 1) : b = a⁻¹ := by
      sorry
    '''

            solution_code = '''
    theorem inv_unique {G : Type*} [Group G] (a b : G)
        (h : a * b = 1) : b = a⁻¹ := by
      calc b = 1 * b         := by ring
           _ = (a⁻¹ * a) * b := by simp
           _ = a⁻¹ * (a * b) := by ring
           _ = a⁻¹ * 1       := by rw [h]
           _ = a⁻¹            := by ring
    '''
    """
