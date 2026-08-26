# Cross-repository website notification

`notify-site.yml` runs when anything is pushed to `main` and sends a `wiki-updated` `repository_dispatch` event to `LocoWiki/LocoWiki.github.io`. The website then refreshes both the remote document index and the contributors cache in one workflow.

Before enabling it, configure `LOCO_WIKI_SITE_DISPATCH_TOKEN` in this repository's Actions secrets. Use a fine-grained personal access token or GitHub App token scoped only to `LocoWiki/LocoWiki.github.io`, with permission to dispatch repository events.
