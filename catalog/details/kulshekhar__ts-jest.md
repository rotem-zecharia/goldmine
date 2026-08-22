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

## Built With

- [TypeScript](https://www.typescriptlang.org/) - JavaScript that scales
- [Jest](https://jestjs.io/) - Delightful JavaScript Testing
- [`ts-jest`](https://kulshekhar.github.io/ts-jest) - Jest [transformer](https://jestjs.io/docs/next/code-transformation#writing-custom-transformers) for TypeScript _(yes, `ts-jest` uses itself for its tests)_

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We **DO NOT** use [SemVer](https://semver.org/) for versioning. Though you can think about SemVer when reading our version, except our major number follows the one of Jest. For the versions available, see the [tags on this repository](https://github.com/kulshekhar/ts-jest/tags).

## Authors/maintainers

- **Kulshekhar Kabra** - [kulshekhar](https://github.com/kulshekhar)
- **Gustav Wengel** - [GeeWee](https://github.com/GeeWee)
- **Ahn** - [ahnpnl](https://github.com/ahnpnl)
- **Huafu Gandon** - [huafu](https://github.com/huafu)

See also the list of [contributors](https://github.com/kulshekhar/ts-jest/contributors) who participated in this project.

## Supporters

- [JetBrains](https://www.jetbrains.com/?from=ts-jest) has been kind enough to support ts-jest with a [license for open source] (https://www.jetbrains.com/community/opensource/?from=ts-jest).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
