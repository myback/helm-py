class _HelmDependency:
    def build(
            self,
            keyring: str = None,
            skip_refresh: bool = None,
            verify: bool = None
    ):
        """Rebuild the charts/ directory based on the Chart.lock file"""
        ...

    def list(self, max_col_width: int = 80):
        """List the dependencies for the given chart"""
        ...

    def update(
            self,
            keyring: str = None,
            skip_refresh: bool = None,
            verify: bool = None
    ):
        """Update charts/ based on the contents of Chart.yaml"""
        ...


class _HelmGet:
    def all(
            self,
            revision: int = None,
            template: str = None
    ):
        """Download all information for a named release"""
        ...

    def hooks(self, revision: int = None):
        """Download all hooks for a named release"""
        ...

    def manifest(self, revision: int = None):
        """Download the manifest for a named release"""
        ...

    def notes(self, revision: int = None):
        """Download the notes for a named release"""
        ...

    def values(
            self,
            all: bool = None,
            output: str = 'table',
            revision: int = None
    ):
        """Download the values file for a named release"""
        ...


class _HelmPlugin:
    def install(self):
        """Install one or more Helm plugins"""
        ...

    def list(self):
        """List installed Helm plugins"""
        ...

    def uninstall(self):
        """Uninstall one or more Helm plugins"""
        ...

    def update(self):
        """Update one or more Helm plugins"""
        ...


class _HelmRegistry:
    def login(
            self,
            host: str,
            insecure: bool = None,
            password: str = None,
            username: str = None
    ):
        """Login to a registry"""
        ...

    def logout(
            self,
            host: str
    ):
        """Logout from a registry"""
        ...


class _HelmRepo:
    def add(
            self,
            name: str,
            url: str,
            allow_deprecated_repos: bool = None,
            ca_file: str = None,
            cert_file: str = None,
            force_update: bool = None,
            insecure_skip_tls_verify: bool = None,
            key_file: str = None,
            pass_credentials: bool = None,
            password: str = None,
            username: str = None,
    ):
        """Add a chart repository"""
        ...

    def index(self, merge: str = None, url: str = None):
        """Generate an index file given a directory containing packaged charts"""
        ...

    def list(self, output: str = 'table'):
        """List chart repositories"""
        ...

    def remove(self, *repo: str):
        """Remove one or more chart repositories"""
        ...

    def update(
            self,
            *repo: str,
            fail_on_repo_update_fail: bool = None
    ):
        """Update information of available charts locally from chart repositories"""
        ...


class _HelmSearch:
    def hub(
            self,
            keyword: str = None,
            endpoint: str = None,
            list_repo_url: str = None,
            max_col_width: int = 50,
            output: str = 'table'
    ):
        """Search for charts in the Artifact Hub or your own hub instance"""
        ...

    def repo(
            self,
            keyword: str = None,
            devel: str = None,
            max_col_width: int = 50,
            output: str = 'table',
            regexp: str = None,
            version: str = None,
            versions: str = None
    ):
        """Search repositories for a keyword in charts"""
        ...


class _HelmShow:
    def all(
            self,
            chart: str = None,
            ca_file: str = None,
            cert_file: str = None,
            devel: str = None,
            insecure_skip_tls_verify: bool = None,
            key_file: str = None,
            keyring: str = None,
            pass_credentials: bool = None,
            password: str = None,
            repo: str = None,
            username: str = None,
            verify: bool = None,
            version: str = None
    ):
        """Show all information of the chart"""
        ...

    def chart(
            self,
            chart: str = None,
            ca_file: str = None,
            cert_file: str = None,
            devel: str = None,
            insecure_skip_tls_verify: bool = None,
            key_file: str = None,
            keyring: str = None,
            pass_credentials: bool = None,
            password: str = None,
            repo: str = None,
            username: str = None,
            verify: bool = None,
            version: str = None
    ):
        """Show the chart's definition"""
        ...

    def crds(
            self,
            chart: str = None,
            ca_file: str = None,
            cert_file: str = None,
            devel: str = None,
            insecure_skip_tls_verify: bool = None,
            key_file: str = None,
            keyring: str = None,
            pass_credentials: bool = None,
            password: str = None,
            repo: str = None,
            username: str = None,
            verify: bool = None,
            version: str = None
    ):
        """Show the chart's CRDs"""
        ...

    def readme(
            self,
            chart: str = None,
            ca_file: str = None,
            cert_file: str = None,
            devel: str = None,
            insecure_skip_tls_verify: bool = None,
            key_file: str = None,
            keyring: str = None,
            pass_credentials: bool = None,
            password: str = None,
            repo: str = None,
            username: str = None,
            verify: bool = None,
            version: str = None
    ):
        """Show the chart's README"""
        ...

    def values(
            self,
            chart: str = None,
            ca_file: str = None,
            cert_file: str = None,
            devel: str = None,
            insecure_skip_tls_verify: bool = None,
            key_file: str = None,
            keyring: str = None,
            pass_credentials: bool = None,
            password: str = None,
            repo: str = None,
            username: str = None,
            verify: bool = None,
            version: str = None
    ):
        """Show the chart's values"""
        ...


class Helm:
    def __init__(
            self,
            debug: bool = None,
            kube_apiserver: str = None,
            kube_as_group: str = None,
            kube_as_user: str = None,
            kube_ca_file: str = None,
            kube_context: str = None,
            kube_token: str = None,
            kubeconfig: str = None,
            namespace: str = None,
            registry_config: str = None,
            repository_cache: str = None,
            repository_config: str = None,
            **kwargs
    ):
        ...

    @property
    def dependency(self) -> _HelmDependency:
        """Manage a chart's dependencies"""
        ...

    def env(self):
        """Helm client environment information"""
        ...

    @property
    def get(self) -> _HelmGet:
        """Download extended information of a named release"""
        ...

    def history(self, max: int = 256, output: str = 'table'):
        """Fetch release history"""
        ...

    def install(
            self,
            *values: str,
            atomic: bool = None,
            ca_file: str = None,
            cert_file: str = None,
            create_namespace: bool = None,
            dependency_update: bool = None,
            description: str = None,
            devel: str = None,
            disable_openapi_validation: bool = None,
            dry_run: bool = None,
            generate_name: bool = None,
            insecure_skip_tls_verify: bool = None,
            key_file: str = None,
            keyring: str = None,
            name_template: str = None,
            no_hooks: bool = None,
            output: str = 'table',
            pass_credentials: bool = None,
            password: str = None,
            post_renderer: str = None,
            post_renderer_args: str = None,
            render_subchart_notes: bool = None,
            replace: bool = None,
            repo: str = None,
            set: str = None,
            set_file: str = None,
            set_string: str = None,
            skip_crds: bool = None,
            timeout: str = None,
            username: str = None,
            verify: bool = None,
            version: str = None,
            wait: bool = None,
            wait_for_jobs: bool = None
    ):
        """Install a chart"""
        ...

    def lint(
            self,
            path: str,
            *values: str,
            quiet: bool = None,
            set: str = None,
            set_file: str = None,
            set_string: str = None,
            strict: bool = None,
            with_subcharts: bool = None
    ):
        """Examine a chart for possible issues"""
        ...

    def list(
            self,
            all: bool = None,
            all_namespaces: bool = None,
            date: bool = None,
            deployed: bool = None,
            failed: bool = None,
            filter: str = None,
            max: int = 256,
            offset: int = None,
            output: str = 'table',
            pending: bool = None,
            reverse: bool = None,
            selector: str = None,
            short: bool = None,
            superseded: bool = None,
            time_format: str = None,
            uninstalled: bool = None,
            uninstalling: bool = None
    ):
        """List releases"""
        ...

    def package(
            self,
            app_version: str = None,
            dependency_update: bool = None,
            destination: str = ".",
            key: str = None,
            keyring: str = None,
            passphrase_file: str = None,
            sign: str = None,
            version: str = None
    ):
        """Package a chart directory into a chart archive"""
        ...

    @property
    def plugin(self) -> _HelmPlugin:
        """Install, list, or uninstall Helm plugins"""
        ...

    def pull(
            self,
            chart: str,
            ca_file: str = None,
            cert_file: str = None,
            destination: str = None,
            devel: bool = None,
            key_file: str = None,
            keyring: str = None,
            pass_credentials: bool = None,
            password: str = None,
            prov: bool = None,
            repo: str = None,
            untar: bool = None,
            untardir: str = None,
            username: str = None,
            verify: bool = None,
            version: str = None,
    ):
        """Download a chart from a repository and (optionally) unpack it in local directory"""
        ...

    def push(self):
        """Push a chart to remote"""
        ...

    @property
    def registry(self) -> _HelmRegistry:
        """Login to or logout from a registry"""
        ...

    @property
    def repo(self) -> _HelmRepo:
        """Add, list, remove, update, and index chart repositories"""
        ...

    def rollback(
            self,
            release: str,
            revision: int = None,
            cleanup_on_fail: bool = None,
            dry_run: bool = None,
            force: bool = None,
            history_max: int = 10,
            no_hooks: bool = None,
            recreate_pods: bool = None,
            timeout: str = None,
            wait: bool = None,
            wait_for_jobs: bool = None
    ):
        """Roll back a release to a previous revision"""
        ...

    @property
    def search(self) -> _HelmSearch:
        """Search for a keyword in charts"""
        ...

    @property
    def show(self) -> _HelmShow:
        """Show information of a chart"""
        ...

    def status(
            self,
            release: str,
            output: str = 'table',
            revision: int = None,
            show_desc: bool = None
    ):
        """Display the status of the named release"""
        ...

    def template(
            self,
            *values: str,
            api_versions: str = None,
            atomic: bool = None,
            ca_file: str = None,
            cert_file: str = None,
            create_namespace: bool = None,
            dependency_update: bool = None,
            description: str = None,
            devel: str = None,
            disable_openapi_validation: bool = None,
            dry_run: bool = None,
            generate_name: bool = None,
            include_crds: bool = None,
            insecure_skip_tls_verify: bool = None,
            is_upgrade: bool = None,
            key_file: str = None,
            kube_version: str = None,
            name_template: str = None,
            no_hooks: bool = None,
            output_dir: str = None,
            pass_credentials: bool = None,
            password: str = None,
            post_renderer: str = None,
            post_renderer_args: str = None,
            release_name: str = None,
            render_subchart_notes: bool = None,
            replace: bool = None,
            repo: str = None,
            set: str = None,
            set_file: str = None,
            set_string: str = None,
            show_only: str = None,
            skip_crds: bool = None,
            skip_tests: bool = None,
            timeout: str = None,
            username: str = None,
            validate: bool = None,
            verify: bool = None,
            version: str = None,
            wait: bool = None,
            wait_for_jobs: bool = None
    ):
        """Locally render templates"""
        ...

    def test(
            self,
            release: str = None,
            filter: str = None,
            logs: bool = None,
            timeout: str = None
    ):
        """Run tests for a release"""
        ...

    def uninstall(
            self,
            release: str,
            description: str = None,
            dry_run: bool = None,
            keep_history: bool = None,
            no_hooks: bool = None,
            timeout: str = None,
            wait: bool = None
    ):
        """Uninstall a release"""
        ...

    def upgrade(
            self,
            *values: str,
            atomic: bool = None,
            ca_file: str = None,
            cert_file: str = None,
            cleanup_on_fail: bool = None,
            create_namespace: bool = None,
            dependency_update: bool = None,
            description: str = None,
            devel: str = None,
            disable_openapi_validation: bool = None,
            dry_run: bool = None,
            force: bool = None,
            history_max: int = 10,
            insecure_skip_tls_verify: bool = None,
            install: bool = None,
            key_file: str = None,
            keyring: str = None,
            no_hooks: bool = None,
            output: str = 'table',
            pass_credentials: bool = None,
            password: str = None,
            post_renderer: str = None,
            post_renderer_args: str = None,
            render_subchart_notes: bool = None,
            replace: bool = None,
            repo: str = None,
            set: str = None,
            set_file: str = None,
            set_string: str = None,
            skip_crds: bool = None,
            timeout: str = None,
            username: str = None,
            verify: bool = None,
            version: str = None,
            wait: bool = None,
            wait_for_jobs: bool = None
    ):
        """Upgrade a release"""
        ...

    def verify(
            self,
            path: str,
            keyring: str = None
    ):
        """Verify that a chart at the given path has been signed and is valid"""
        ...

    def version(self):
        """Print the client version information"""
        ...
