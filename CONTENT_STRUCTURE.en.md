# Content Structure and Website Boundary

This repository is LocoWiki's robotics knowledge source. Website code, visual styling, and interface copy do not belong here.

| Content type | Directory | Website collection |
| --- | --- | --- |
| Tutorials and knowledge articles | `wiki/` | Docs |
| Competition rules and related notes | `competition-rules/` | Docs |
| Team technical sharing | `technical-sharing/` | Docs |
| Script usage documentation | `scripts/` | Docs |
| Paper metadata, notes, and original links | `reading-list/` | Papers |
| Open-source projects and learning-resource indexes | `network-open-source/` | Open Source |

## Open-Source Responsibilities

- `network-open-source/README.md`: the unified index for complete competition solutions, core drivers, competition resources, learning knowledge bases, and independent project articles.
- `network-open-source/*.md`: concrete repositories, hardware, datasets, tools, paper reproductions, and team projects; explain what the project is and where/how to access it.
- `wiki/`: general theory, training methods, controller design, and engineering experience. Citing a team repository does not require moving the tutorial.
- `reading-list/`: paper titles, authors, abstracts, original links, and reading status. Link related code without duplicating the project article.

## Content that belongs elsewhere

- Copy for Home, About, Downloads, and Contributors
- Website navigation, styles, search, themes, and page code
- Website maintenance and developer documentation

Submit these changes to `LocoWiki/LocoWiki.github.io`.

## Adding material

1. Choose a directory from the table. Do not add website-facing Markdown at the repository root.
2. Prefer official pages, original authors, open-access platforms, or upstream open-source repositories.
3. Use the `.en.md` suffix for paired English files.
4. Once merged, the website repository refreshes its index automatically; individual articles do not need manual registration there.
