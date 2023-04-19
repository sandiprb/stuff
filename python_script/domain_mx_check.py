import logging

# Note: dnspython dependency is required for this to work
import dns.resolver, dns.exception
import sys

print(sys.argv)

logger = logging.getLogger(__name__)

def is_valid_domain(domain):
    try:
        logger.debug('Checking domain %s', domain)
        dns.resolver.query(domain, 'MX')
        return True
    except dns.exception.DNSException as e:
        logger.debug('Domain %s does not exist.', e)
        return False
