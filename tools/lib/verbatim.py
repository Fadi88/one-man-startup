"""Files copied verbatim from upstream, pinned by hash (TPL-17).

Each entry: path -> (marker, sha256). The hash covers the text from the marker
line to the end of the file; an empty marker means the whole file. Verbatim
files are exempt from the style check because changing them would break the
copy; their wrappers in this repository follow the style rules.
"""

PINNED = {
    # forrestchang/andrej-karpathy-skills CLAUDE.md, fetched 2026-10-14.
    "skills/karpathy-guidelines/SKILL.md": (
        "# CLAUDE.md",
        "694a2d721e41c385f3db492838c23299826df5ba9809e3b0721aac70021e196a",
    ),
    # anthropics/claude-plugins-official plugins/frontend-design/skills/frontend-design/SKILL.md,
    # copied 2026-10-14, Apache License 2.0.
    "skills/frontend-design/UPSTREAM.md": (
        "",
        "d91970639e9f5c37682ac7ab60094d35f1c7c1f38d731bd56396563aee10c1d3",
    ),
}
