#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    """
    keep all messages in en

    Returns:
        all messages in JSON
    """
    return \
        {
            "scan_started": "Nettacker engine started ...\n\n",
            "options": "python nettacker.py [options]",
            "help_menu": "Show Nettacker Help Menu",
            "license": "Please read license and agreements https://github.com/zdresearch/OWASP-Nettacker\n",
            "engine": "Engine",
            "engine_input": "Engine input options",
            "select_language": "select a language {0}",
            "range": "scan all IPs in the range",
            "subdomains": "find and scan subdomains",
            "thread_number_connections": "thread numbers for connections to a host",
            "thread_number_hosts": "thread numbers for scan hosts",
            "save_logs": "save all logs in file (results.txt, results.html, results.json)",
            "target": "Target",
            "target_input": "Target input options",
            "target_list": "target(s) list, separate with \",\"",
            "read_target": "read target(s) from file",
            "scan_method_options": "Scan method options",
            "choose_scan_method": "choose scan method {0}",
            "exclude_scan_method": "choose scan method to exclude {0}",
            "username_list": "username(s) list, separate with \",\"",
            "username_from_file": "read username(s) from file",
            "password_seperator": "password(s) list, separate with \",\"",
            "read_passwords": "read password(s) from file",
            "port_seperator": "port(s) list, separate with \",\"",
            "time_to_sleep": "time to sleep between each request",
            "error_target": "Cannot specify the target(s)",
            "error_target_file": "Cannot specify the target(s), unable to open file: {0}",
            "thread_number_warning": "it's better to use thread number lower than 100, BTW we are continuing...",
            "set_timeout": "set timeout to {0} seconds, it is too big, isn't it ? by the way we are continuing...",
            "scan_module_not_found": "this scan module [{0}] not found!",
            "error_exclude_all": "you cannot exclude all scan methods",
            "exclude_module_error": "the {0} module you selected to exclude not found!",
            "method_inputs": "enter methods inputs, example: ftp_brute_users=test,admin&ftp_brute_passwds="
                             "read_from_file:/tmp/pass.txt&ftp_brute_port=21",
            "error_reading_file": "cannot read file {0}",
            "error_username": "Cannot specify the username(s), unable to open file: {0}",
            "found": "{0} found! ({1}:{2})",
            "error_password_file": "Cannot specify the password(s), unable to open file: {0}",
            "file_write_error": "file \"{0}\" is not writable!",
            "scan_method_select": "please choose your scan method!",
            "remove_temp": "removing temp files!",
            "sorting_results": "sorting results!",
            "done": "done!",
            "start_attack": "start attacking {0}, {1} of {2}",
            "module_not_available": "this module \"{0}\" is not available",
            "error_platform": "unfortunately this version of the software could only be run on linux/osx/windows.",
            "python_version_error": "Your Python version is not supported!",
            "skip_duplicate_target": "skip duplicate target (some subdomains/domains may have same IP and Ranges)",
            "unknown_target": "unknown type of target [{0}]",
            "checking_range": "checking {0} range ...",
            "checking": "checking {0} ...",
            "HOST": "HOST",
            "USERNAME": "USERNAME",
            "PASSWORD": "PASSWORD",
            "PORT": "PORT",
            "TYPE": "TYPE",
            "DESCRIPTION": "DESCRIPTION",
            "verbose_level": "verbose mode level (0-5) (default 0)",
            "software_version": "show software version",
            "check_updates": "check for update",
            "outgoing_proxy": "outgoing connections proxy (socks). example socks5: 127.0.0.1:9050, "
                              "socks://127.0.0.1:9050 socks5://127.0.0.1:9050 or socks4: socks4://127.0.0.1:9050,"
                              " authentication: socks://username: password@127.0.0.1, socks4://username:password@"
                              "127.0.0.1, socks5://username:password@127.0.0.1",
            "valid_socks_address": "please enter valid socks address and port. example socks5:"
                                   " 127.0.0.1:9050, socks://127.0.0.1:9050, socks5://127.0.0.1:9050 "
                                   "or socks4: socks4://127.0.0.1:9050, authentication: socks://username:password"
                                   "@127.0.0.1, socks4://username:password@127.0.0.1, "
                                   "socks5://username:password@127.0.0.1",
            "connection_retries": "Retries when the connection timeout (default 3)",
            "ftp_connection_timeout": "ftp connection to {0}:{1} timeout, skipping {2}:{3}",
            "login_successful": "LOGGED IN SUCCESSFULLY!",
            "login_list_error": "LOGGED IN SUCCESSFULLY, PERMISSION DENIED FOR LIST COMMAND!",
            "ftp_connection_failed": "ftp connection to {0}:{1} failed, skipping whole step "
                                     "[process {2} of {3}]! going to next step",
            "input_target_error": "input target for {0} module must be DOMAIN, HTTP or SINGLE_IPv4, skipping {1}",
            "user_pass_found": "user: {0} pass:{1} host:{2} port:{3} found!",
            "file_listing_error": "(NO PERMISSION FOR LIST FILES)",
            "trying_message": "trying {0} of {1} in process {2} of {3} {4}:{5} ({6})",
            "smtp_connection_timeout": "smtp connection to {0}:{1} timeout, skipping {2}:{3}",
            "smtp_connection_failed": "smtp connection to {0}:{1} failed, skipping whole step "
                                      "[process {2} of {3}]! going to next step",
            "ssh_connection_timeout": "ssh connection to {0}:{1} timeout, skipping {2}:{3}",
            "ssh_connection_failed": "ssh connection to {0}:{1} failed, skipping whole step"
                                     " [process {2} of {3}]! going to next step",
            "port/type": "{0}/{1}",
            "port_found": "host: {0} port: {1} ({2}) found!",
            "target_submitted": "target {0} submitted!",
            "current_version": "you are running OWASP Nettacker version {0}{1}{2}{6} with code name {3}{4}{5}",
            "feature_unavailable": "this feature is not available yet! please run \"git clone "
                                   "https://github.com/zdresearch/OWASP-Nettacker.git or pip install"
                                   " -U OWASP-Nettacker to get the latest version.",
            "available_graph": "build a graph of all activities and information, you must"
                               " use HTML output. available graphs: {0}",
            "graph_output": "to use graph feature your output filename must end with \".html\" or \".htm\"!",
            "build_graph": "building graph ...",
            "finish_build_graph": "finish building graph!",
            "pentest_graphs": "Penetration Testing Graphs",
            "graph_message": "This graph created by OWASP Nettacker. Graph contains all"
                             " modules activities, network map and sensitive information,"
                             " Please don't share this file with anyone if it's not reliable.",
            "nettacker_report": "OWASP Nettacker Report",
            "nettacker_version_details": "Software Details: OWASP Nettacker version {0} [{1}] in {2}",
            "no_open_ports": "no open ports found!",
            "no_user_passwords": "no user/password found!",
            "loaded_modules": "{0} modules loaded ...",
            "graph_module_404": "this graph module not found: {0}",
            "graph_module_unavailable": "this graph module \"{0}\" is not available",
            "ping_before_scan": "ping before scan the host",
            "skipping_target": "skipping whole target {0} and scanning method {1} because of "
                               "--ping-before-scan is true and it didn't response!",
            "not_last_version": "you are not using the latest version of OWASP Nettacker, please update.",
            "cannot_update": "cannot check for update, please check your internet connection.",
            "last_version": "You are using the latest version of OWASP Nettacker ...",
            "directoy_listing": "directory listing found in {0}",
            "insert_port_message": "please insert port through the -g or --methods-args switch instead of url",
            "http_connection_timeout": "http connection {0} timeout!",
            "wizard_mode": "start wizard mode",
            "directory_file_404": "no directory or file found for {0} in port {1}",
            "open_error": "unable to open {0}",
            "dir_scan_get": "dir_scan_http_method value must be GET or HEAD, set default to GET.",
            "list_methods": "list all methods args",
            "module_args_error": "cannot get {0} module args",
            "trying_process": "trying {0} of {1} in process {2} of {3} on {4} ({5})",
            "domain_found": "domain found: {0}",
            "TIME": "TIME",
            "CATEGORY": "CATEGORY",  # not used
            "module_pattern_404": "cannot find any module with {0} pattern!",
            "enter_default": "please enter {0} | Default[{1}] > ",
            "enter_choices_default": "please enter {0} | choices[{1}] | Default[{2}] > ",
            "all_targets": "the targets",
            "all_thread_numbers": "the thread number",
            "out_file": "the output filename",
            "all_scan_methods": "the scan methods",
            "all_scan_methods_exclude": "the scan methods to exclude",
            "all_usernames": "the usernames",
            "all_passwords": "the passwords",
            "timeout_seconds": "the timeout seconds",
            "Invalid_shodan_api_key": "{0}",
            "shodan_api_key": "Shodan api key for shodan recon",
            "shodan_results_found": "Found results: {0}",
            "shodan_results_not_found": "Didn't found anything in the shodan database",
            "shodan_plan_upgrade": "Please upgrade your API plan to use FILTERS or PAGING and getting much better results",
            "searching_shodan_database": "Searching Shodan Database...",
            "all_ports": "the port numbers",
            "all_verbose_level": "the verbose level",
            "all_socks_proxy": "the socks proxy",
            "retries_number": "the retries number",
            "graph": "a graph",
            "subdomain_found": "subdomain found: {0}",
            "select_profile": "select profile {0}",
            "profile_404": "the profile \"{0}\" not found!",
            "waiting": "waiting for {0}",
            "vulnerable": "vulnerable to {0}",
            "target_vulnerable": "target {0}:{1} is vulnerable to {2}!",
            "no_vulnerability_found": "no vulnerability found! ({0})",
            "Method": "Method",
            "API": "API",
            "API_options": "API options",
            "start_API": "start the API service",
            "API_host": "API host address",
            "API_port": "API port number",
            "API_debug": "API debug mode",
            "API_access_key": "API access key",
            "white_list_API": "just allow white list hosts to connect to the API",
            "define_whie_list": "define white list hosts, separate with , (examples: "
                                "127.0.0.1, 192.168.0.1/24, 10.0.0.1-10.0.0.255)",
            "gen_API_access_log": "generate API access log",
            "API_access_log_file": "API access log filename",
            "API_port_int": "API port must be an integer!",
            "unknown_ip_input": "unknown input type, accepted types are SINGLE_IPv4, RANGE_IPv4, CIDR_IPv4",
            "API_key": " * API Key: {0}\n",
            "ports_int": "ports must be integers! (e.g. 80 || 80,1080 || 80,1080-1300,9000,12000-15000)",
            "through_API": "Through the OWASP Nettacker API",
            "API_invalid": "invalid API key",
            "unauthorized_IP": "your IP not authorized",
            "not_found": "Not Found!",
            "no_subdomain_found": "subdomain_scan: no subdomain found!",
            "viewdns_domain_404": "viewdns_reverse_ip_lookup_scan: no domain found!",
            "browser_session_valid": "your browser session is valid",
            "browser_session_killed": "your browser session killed",
            "updating_database": "updating the database...",
            "database_connect_fail": "could not connect to the database!",
            "inserting_report_db": "inserting report to the database",
            "inserting_logs_db": "inserting logs to the database",
            "removing_logs_db": "removing old logs from db",
            "len_subdomain_found": "{0} subdomain(s) found!",
            "len_domain_found": "{0} domain(s) found!",
            "phpmyadmin_dir_404": "not any phpmyadmin dir found!",
            "DOS_send": "sending DoS packets to {0}",
            "host_up": "{0} is up! Time taken to ping back is {1}",
            "host_down": "Cannot ping {0}!",
            "root_required": "this needs to be run as root",
            "admin_scan_get": "admin_scan_http_method value must be GET or HEAD, set default to GET.",
            "telnet_connection_timeout": "telnet connection to {0}:{1} timeout, skipping {2}:{3}",
            "telnet_connection_failed": "telnet connection to {0}:{1} failed, "
                                        "skipping whole step [process {2} of {3}]! going to next step",
            "http_auth_success": "http basic authentication success - host:{2}:{3}, user: {0}, pass:{1} found!",
            "http_auth_failed": "http basic authentication failed to {0}:{3} using {1}:{2}",
            "http_form_auth_success": "http form authentication success - host:{2}:{3}, user: {0}, pass:{1} found!",
            "http_form_auth_failed": "http form authentication failed to {0}:{3} using {1}:{2}",
            "using_shodan_query_override": "Using {0} as a target",
            "http_ntlm_success": "http ntlm authentication success - host:{2}:{3}, user: {0}, pass:{1} found!",
            "http_ntlm_failed": "http ntlm authentication failed to {0}:{3} using {1}:{2}",
            "no_response": "cannot get response from target",
            "category_framework": "category: {0}, frameworks: {1} found!",
            "nothing_found": "nothing found on {0} in {1}!",
            "no_auth": "No auth found on {0}:{1}",
            "invalid_database": "Please select from mysql or sqlite in the configuration file",
            "database_connection_failed": "Connection to the selected db failed",
            "fuzzer_no_response": "The http fuzzer did not find any output for {0}",
            "summary_report": "summary report table",
            "file_saved": "report saved in {0} and database",
            "no_event_found": "no event found in this scan",
            "invalid_json_type_to_db": "Invalid type of JSON data for the database. Skipping the submission to database"
                                       ". Data:{0}"
        }
