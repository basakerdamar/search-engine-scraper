library(ggplot2)

ad_url_count <- read.csv('ad_url_count')
ggplot(ad_url_count, aes(x = reorder(ad_url, -count), y = count)) + 
  geom_bar(stat = "identity") + 
  theme(axis.text.x=element_text(angle=5,hjust=1, size = 6))  + 
  ggtitle("") # for the main title

browser_adcount <- read.csv('browser_adcount')
ggplot(browser_adcount, aes(x = reorder(Browser, -count), y = count)) +
geom_bar(stat = "identity") + 
  theme(axis.text.x=element_text(angle=30,hjust=1)) + ggtitle("") + 
  xlab("Browser") + ylab("Count")

cookie_consent_count <- read.csv('cookie_consent_count')
ggplot(cookie_consent_count, aes(x = cookie_consent, y = count)) +
geom_bar(stat = "identity") + 
   xlab("Cookie Consent Given") + ylab("Advertisement Count")

search_url_ad_count <- read.csv('search_url_ad_count')
ggplot(search_url_ad_count, aes(x = reorder(search_url, -count), y = count)) + 
geom_bar(stat = "identity") + 
  theme(axis.text.x=element_text(angle=60,hjust=1)) + ggtitle("") + 
  xlab("Search Query") + ylab("Advertisement Count")

user_count <- read.csv('Seminar/Data/user_count')
ggplot(user_count, aes(x = reorder(user_type, -count), y = count)) + 
geom_bar(stat = "identity") + 
    ggtitle("") + xlab("User type") + ylab("Advertisement Count")
 
query_count <- read.csv('query_count')
ggplot(query_count, aes(x = reorder(query_type, -count), y = count)) + 
geom_bar(stat = "identity") + 
  ggtitle("") + xlab("Query type") + ylab("Advertisement Count")

exp_user_ad_url <- read.csv('exp_user_ad_url')
ggplot(exp_user_ad_url, aes(x = reorder(ad_url, -count), y = count)) + 
geom_bar(stat = "identity") + 
  ggtitle("The most frequent advertisements for \"expensive\" users") +
   xlab("Advertisement URL") + ylab("Advertisement Count") +  
  theme(axis.text.x=element_text(angle=30,hjust=1)) + 
  theme(plot.title = element_text(hjust = 0.5))

cheap_user_ad_url <- read.csv('cheap_user_ad_url')
ggplot(cheap_user_ad_url, aes(x = reorder(ad_url, -count), y = count)) + 
geom_bar(stat = "identity") + 
  ggtitle("The most frequent advertisements for \"cheap\" users") + 
  xlab("Advertisement URL") + ylab("Advertisement Count") +  
  theme(axis.text.x=element_text(angle=30,hjust=1)) + 
  theme(plot.title = element_text(hjust = 0.5))

user_query_count <- read.csv('user_query_count')
# query  odaklı:
ggplot(user_query_count, 
  aes(x = reorder(query_type, -count), y = count, fill = user_type )) + 
  geom_bar(stat = "identity") + 
  ggtitle("") + xlab("Query type") + ylab("Advertisement Count") + 
  labs(fill = "User type")
# user odaklı:
ggplot(user_query_count, aes(x = reorder(user_type, -count), 
  y = count, fill = query_type  )) + geom_bar(stat = "identity") + 
  ggtitle("") + xlab("User type") + ylab("Advertisement Count") + 
  labs(fill = "Query type:")
