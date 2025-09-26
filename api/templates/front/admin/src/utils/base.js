const base = {
    get() {
        return {
            url : "http://localhost:8080/python7n2a3/",
            name: "python7n2a3",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/python7n2a3/front/dist/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "中小学生情绪管理平台"
        } 
    }
}
export default base
