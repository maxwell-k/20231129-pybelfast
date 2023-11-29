<!--
SPDX-License-Identifier: CC-BY-NC-SA-4.0
SPDX-FileCopyrightText: 2023 Keith Maxwell
-->

<!-- https://www.canva.com/colors/color-palettes/healthy-leaves/ -->
<style>
:root {
    --custom-one: #3D550C;
    --custom-two: #81B622;
    --custom-three: #ECF87F;
    --custom-four: #59981A;
    --h1-color: var(--custom-one);
    /* --color-fg-default: black; */
}
</style>

<style scoped>
div.columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    place-items: center start;
}
</style>

<div class=columns>
<div>

A

- One
- Two
- Three
- Four

</div>

<div>

Centered vertically

<div>
</div>

---

<style scoped>
div.columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
}
</style>

<div class=columns>
<div>

A

- One
- Two
- Three
- Four

</div>

<div>

B

- Alpha
- Bravo
- Charlie
- Delta

<div>
</div>

---

Horizontal rule

<hr />

---

# Heading Level 1

## Heading Level 2

### Heading Level 3

---

```python
def python_code():
    pass
```

Paragraph

---

- Simple
- Bullet
- List

---

# Bullets point list items that show one by one

<!-- prettier-ignore-start -->

<div>

* Asterisks show as individual bullet points
* User prettier-ignore-start/end
* So that asterisks are not reformatted

</div>

<!-- prettier-ignore-end -->

---

# Ordered list items that appear one-by-one

<!-- prettier-ignore -->
1) One
2) Two
3) Three
4) Four
5) Five

<div data-marpit-fragment>

Bonus paragraph.

</div>

---

# Two columns

<style scoped>
.columns {
    display:flex;
    flex-wrap:wrap;
}

.columns > * {
    width:50%;
}
</style>

<div class="columns">

<div>

1. One
2. Two
3. Three
4. Four
5. Five
6. Six
7. Seven
8. Eight
9. Nine
10. Ten

</div>

<div>

11. Eleven
12. Twelve
13. Thirteen
14. Fourteen
15. Fifteen
16. Sixteen
17. Seventeen
18. Eighteen
19. Nineteen
20. Twenty

</div>

---

<!-- _backgroundColor: var(--custom-one) -->
<!-- _color: white -->

Bespoke colours per slide

---

<!-- _backgroundColor: var(--custom-three) -->
<!-- _color: black -->

More colours

---

# <!-- fit --> Fill line horizontally

---

# <!-- fit --> Fill line horizontally<br /> Continuation

---

# Blocks that appear step-by-step

<div data-marpit-fragment>

## Block one heading

- One,
- Two and
- Three all appear together wit the block heading

</div data-marpit-fragment>

<div data-marpit-fragment>

Block two

</div data-marpit-fragment>

---

# Table

| A   | B   | C   |
| --- | --- | --- |
| One | 1   | 2   |
|     | 3   | 4   |
| Two | 5   | 6   |

---

Comments appear in the presenter console

<!--

Comments appear in the presenter console

Another name for these is speaker notes

-->

---

Image

![](https://picsum.photos/200)

---

# Scaled image

<style scoped>
img { width: 100%; }
</style>

![](https://picsum.photos/600/300)

---

# Small print

<style scoped>
p {
    font-size: 0.5em;
}
</style>

_Text_

---

Emoji

:smile:

---

<style scoped>
p { font-size: 3em; }
</style>

_Custom font-size_

---

Fill in the gaps

# 1. Heading

<!-- prettier-ignore -->
* one
* two
* three

# 2. Heading

<!-- prettier-ignore -->
* four
* five
* six
* seven
* eight

---

<!-- _backgroundColor: var(--custom-one) -->
<!-- _color: white -->

# Code block against a dark background

<div style="color: black">

```
>>> 1024**3 / 1000**3 - 1
0.07374182400000007
```

</div>

---

> This is a quote

— _Attribution_

---

# Checklist

<style scoped>
ul {
  list-style: none;
}
</style>

- ☐ One
- ☐ Two

---

<!--

https://marpit.marp.app/image-syntax?id=slide-backgrounds

-->

![bg](https://picsum.photos/3000)

---

# Features that don't work for me:

Inverted slide

```
<!-- class: invert -->
```

<!-- vim: set filetype=markdown.gfm.htmlCommentNoSpell : -->
