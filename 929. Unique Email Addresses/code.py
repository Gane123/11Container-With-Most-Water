class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsSet = set()
        for i in emails:
            emailList,domain = i.split("@")
            if "+" or "." in emailList:
                emailListwithoutplus = emailList.split("+")[0]
                emailListwithoutplusandpoint = emailListwithoutplus.replace(".","")
                emailsSet.add("@".join([emailListwithoutplusandpoint,domain]))
            else:
                emailsSet.add(i)
        return len(emailsSet)
