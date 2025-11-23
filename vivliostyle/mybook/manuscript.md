# Brief History of JavaScript

リンクのある後注の例：
VFM is developed in the GitHub repository[^1].
Issues are managed on GitHub[^issues].
Endnotes can also be written inline^[This part is a endnote.].

[^1]: [VFM](https://github.com/vivliostyle/vfm)
[^issues]: [Issues](https://github.com/vivliostyle/vfm/issues)

from Wikipedia <https://en.wikipedia.org/wiki/JavaScript>

https://example.com/

「さよなら。」って、その子は花<span class="footnote">この部分が脚注になります。</span>に言った。

<nav id="toc" role="doc-toc">
</nav>

## JavaScript

**JavaScript** (`/ˈdʒɑːvəˌskrɪpt/`),often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.

JavaScript is _high-level_, often just-in-time compiled, and multi-paradigm. It has curly-bracket syntax, dynamic typing, prototype-based object-orientation, and first-class functions.

### Weakly typed

JavaScript is weakly typed, which means certain types are implicitly cast depending on the operation used.

- The binary `+` operator casts both operands to a string unless both operands are numbers. This is because the addition operator doubles as a concatenation operator
- The binary `-` operator always casts both operands to a number
- Both unary operators (+, -) always cast the operand to a number

#### JavaScript includes a number of quirks that have been subject to criticism

| left operand     | operator | right operand     | result                     |
| ---------------- | -------- | ----------------- | -------------------------- |
| [](empty array)  | +        | [](empty array)   | ""(empty string)           |
| [] (empty array) | +        | {} (empty object) | "[object Object]" (string) |
| false (boolean)  | +        | [] (empty array)  | "false" (string)           |
| "123"(string)    | +        | 1 (number)        | "1231" (string)            |
| "123" (string)   | -        | 1 (number)        | 122 (number)               |

```javascript
('b' + 'a' + +'a' + 'a').toLowerCase(); // "banana"
```
