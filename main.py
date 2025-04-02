import requests
 
# 在这里填入你的个人访问令牌,令牌地址可以通过访问 http://git.xxx.com/api/swagger，用你的账号密码登录获得
# 访问令牌需要有管理员权限
access_token = "aabbccddeeffxxxxxx"
user_name = "test"
base_url = "http://git.xxx.com/api/v1/"

def get_user_list():
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(base_url+"admin/users", headers=headers)
    #print(response)
    users = response.json()
    return users
 


# 获取仓库列表
def get_repository_list(user_name):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(base_url+"users/"+user_name+"/repos", headers=headers)
    #print(response)
    repositories = response.json()
    return repositories
 
# 删除仓库
def delete_repository(user_name,repo_name):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    del_uri=base_url+f"repos/{user_name}/{repo_name}"
    print("Del repos:",del_uri)
    #return
    response = requests.delete(del_uri, headers=headers)
    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully.")
    else:
        print(f"Failed to delete repository '{repo_name}'. Status code: {response.status_code}")

def delete_user(user_name):
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    del_uri=base_url+f"admin/users/{user_name}"
    print("Del User:",del_uri)
    #return
    response = requests.delete(del_uri, headers=headers)
    if response.status_code == 204:
        print(f"User '{user_name}' deleted successfully.")
    else:
        print(f"Failed to delete user '{user_name}'. Status code: {response.status_code}")


if __name__ == "__main__":
    users=  get_user_list()
    excludeUsers = ["user1","user2",	"user3", "user4"]  # 排除用户列表，将要保留的用户名称放在这里
    for user in users:
        if user["login"] in excludeUsers:
            continue
        print("------user:",user["login"])
        user_name = user["login"]
        repositories = get_repository_list(user_name)
        print(len(repositories))
        for repo in repositories:
            repo_name = repo["name"]
            print("----repo_name:",repo_name)
            delete_repository(user_name,repo_name)
        delete_user(user_name)
    
