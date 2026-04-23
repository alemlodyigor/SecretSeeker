import datetime
def json_reporter(findings):
    findings_len = len(findings)
    date = datetime.datetime.now()
    report = {
        'summary': {
            'total_findings': findings_len,
            'scan_date': date.isoformat(),
        },
        'results': []
    }

    for finding in findings:
        result = {
            'file': finding['file'],
            'line': finding['line'],
            'detector': finding['detector'],
            'type': finding['type'],
            'value': finding['value']
        }

        if 'entropy' in finding:
            result['entropy'] = finding['entropy']

        report['results'].append(result)

    return report