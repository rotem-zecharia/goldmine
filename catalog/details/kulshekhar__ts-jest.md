# kulshekhar/ts-jest

A Jest transformer with source map support that lets you use Jest to test projects written in TypeScript.

## installation

These instructions will get you setup to use `ts-jest` in your project. For more detailed documentation, please check [online documentation](https://kulshekhar.github.io/ts-jest).

|                                      | using npm                      | using yarn                           |
| -----------------------------------: | ------------------------------ | ------------------------------------ |
| **Prerequisites (TypeScript 4.3–6)** | `npm i -D jest typescript`     | `yarn add --dev jest typescript`     |
|                       **Installing** | `npm i -D ts-jest @types/jest` | `yarn add --dev ts-jest @types/jest` |
|                  **Creating config** | `npx ts-jest config:init`      | `yarn ts-jest config:init`           |
|                    **Running tests** | `npm test` or `npx jest`       | `yarn test` or `yarn jest`           |

If your project uses TypeScript 7, follow the [supported side-by-side compiler setup](website/docs/guides/typescript-7.md)
instead of installing `typescript` directly.
