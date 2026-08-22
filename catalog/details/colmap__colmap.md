# colmap/colmap

COLMAP - Structure-from-Motion and Multi-View Stereo

## installation

1. Download pre-built binaries or build from source.
2. Download one of the provided [sample datasets](https://demuc.de/colmap/datasets/)
   or use your own images.
3. Use the **automatic reconstruction** to easily build models
   with a single click or command.

Documentation
-------------

The documentation is available [here](https://colmap.github.io/).

To build and update the documentation at the documentation website,
follow [these steps](https://colmap.github.io/install.html#documentation).

Support
-------

Please, use [GitHub Discussions](https://github.com/colmap/colmap/discussions)
for questions and the [GitHub issue tracker](https://github.com/colmap/colmap)
for bug reports, feature requests/additions, etc.

Acknowledgments
---------------

COLMAP was originally written by [Johannes Schönberger](https://demuc.de/) with
funding provided by his PhD advisors Jan-Michael Frahm and Marc Pollefeys.
The team of core project maintainers currently includes
[Johannes Schönberger](https://github.com/ahojnnes),
[Paul-Edouard Sarlin](https://github.com/sarlinpe),
[Shaohui Liu](https://github.com/B1ueber2y), and
[Linfei Pan](https://lpanaf.github.io/).

The Python bindings in PyCOLMAP were originally added by
[Mihai Dusmanu](https://github.com/mihaidusmanu),
[Philipp Lindenberger](https://github.com/Phil26AT), and
[Paul-Edouard Sarlin](https://github.com/sarlinpe).

The project has also benefitted from countless community contributions, including
bug fixes, improvements, new features, third-party tooling, and community
support (special credits to [Torsten Sattler](https://tsattler.github.io)).

Citation
--------

If you use this project for your research, please cite:

    @inproceedings{schoenberger2016sfm,
        author={Sch\"{o}nberger, Johannes Lutz and Frahm, Jan-Michael},
        title={Structure-from-Motion Revisited},
        booktitle={Conference on Computer Vision and Pattern Recognition (CVPR)},
        year={2016},
    }

    @inproceedings{schoenberger2016mvs,
        author={Sch\"{o}nberger, Johannes Lutz and Zheng, Enliang and Pollefeys, Marc and Frahm, Jan-Michael},
        title={Pixelwise View Selection for Unstructured Multi-View Stereo},
        booktitle={European Conference on Computer Vision (ECCV)},
        year={2016},
    }

If you use the global SfM pipeline (GLOMAP), please cite:

    @inproceedings{pan2024glomap,
        author={Pan, Linfei and Barath, Daniel and Pollefeys, Marc and Sch\"{o}nberger, Johannes Lutz},
        title={{Global Structure-from-Motion Revisited}},
        booktitle={European Conference on Computer Vision (ECCV)},
        year={2024},
    }

If you use the image retrieval / vocabulary tree engine, please cite:

    @inproceedings{schoenberger2016vote,
        author={Sch\"{o}nberger, Johannes Lutz and Price, True and Sattler, Torsten and Frahm, Jan-Michael and Pollefeys, Marc},
        title={A Vote-and-Verify Strategy for Fast Spatial Verification in Image Retrieval},
        booktitle={Asian Conference on Computer Vision (ACCV)},
        year={2016},
    }

Contribution
------------

Contributions (bug reports, bug fixes, improvements, etc.) are very welcome and
should be submitted in the form of new issues and/or pull requests on GitHub.

License
-------

The COLMAP library is licensed under the new BSD license. Note that this text
refers only to the license for COLMAP itself, independent of its thirdparty
dependencies, which are separately licensed. Building COLMAP with these
dependencies may affect the resulting COLMAP license.

    Copyright (c), ETH Zurich and UNC Chapel Hill.
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:

        * Redistributions of source code must retain the above copyright
          notice, this list of conditions and the following disclaimer.

        * Redistributions in binary form must reproduce the above copyright
