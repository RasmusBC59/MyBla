def _get_version() -> str:
    from pathlib import Path

    import versioningit

    import mybla

    mybla_path = Path(mybla.__file__).parent
    return versioningit.get_version(project_dir=mybla_path.parent)


__version__ = _get_version()
