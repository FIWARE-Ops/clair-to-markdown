# clair-to-markdown

Action to translate a [clair-scan report](https://github.com/quay/clair) into a [markdown-file](https://en.wikipedia.org/wiki/Markdown), as for example supported by github.

## Example usage

```yaml
uses: fiware/clair-to-markdown@master
with:
    markdownFile: "/github/workspace/README.md
```
