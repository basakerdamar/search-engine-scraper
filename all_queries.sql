drop table advertisements;

create table advertisements(
id serial,
search_url text, 
ad_url text , 
query_type char(1), 
user_type char(1), 
user_agent text, 
cookie_consent char(3));

/*browser_adcount*/
select distinct user_agent, count(*) over ( PARTITION BY user_agent ) from advertisements
order by count desc;

select distinct user_agent, search_url, count(*) over ( PARTITION BY user_agent, search_url ) from advertisements
order by count desc;


/*search_url_ad_count*/
select distinct search_url, count(*) over ( PARTITION BY search_url ) from advertisements
order by count desc limit 20;


/*ad_url_count*/
select ad_url, count(ad_url) from advertisements
group by ad_url
order by count desc limit 20; 

/* cheap_user_ad_url */
select ad_url, count(ad_url) from advertisements
where user_type = 'C'
group by ad_url
order by count desc
limit 20; 

/* exp_user_ad_url */
select ad_url, count(ad_url) from advertisements
where user_type = 'E'
group by ad_url
order by count desc
limit 20; 

/*cookie_consent_count*/
select distinct cookie_consent, count(*) over ( PARTITION BY cookie_consent ) from advertisements
order by count desc;

select distinct search_url, ad_url, count(*) over ( PARTITION BY search_url, ad_url ) from advertisements
order by count desc limit 20;

/* user_query_count*/
select distinct user_type, query_type, count(*) over (partition by user_type, query_type) from advertisements
order by count desc;

/*user_count*/
select distinct user_type, count(*) over (partition by user_type) from advertisements
order by count desc;

/* query_count */
select distinct query_type, count(*) over (partition by query_type) from advertisements
order by count desc;
  
select search_url, ad_url from advertisements where ad_url like '%&adurl%';
select count(*) from advertisements where ad_url like '%adurl%';

select count(distinct ad_url) from advertisements;
select count(distinct search_url) from advertisements;
select count(*) from advertisements;
