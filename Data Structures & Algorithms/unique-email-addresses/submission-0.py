class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.replace(".", "")
            clean_email = local_name + "@" + domain_name
            unique_emails.add(clean_email)

        return len(unique_emails)