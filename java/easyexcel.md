#### 最近在用 easyexcel 导入数据



#### 1、[不创建对象的读](https://www.yuque.com/easyexcel/doc/read#f14acd88)

```java
// 示例相见说明文档。
// 遇到的问题: 在调用saveData 将数据写入到数据库, NullPointerException 空指针
import org.springframework.stereotype.Component;
/**
 * 直接用map接收数据
 *
 * @author Jiaju Zhuang
 
 */
// Component 写入到BeanFactory 进行管理
@Component
public class NoModelDataListener extends AnalysisEventListener<Map<Integer, String>> {
    private static final Logger LOGGER = LoggerFactory.getLogger(NoModelDataListener.class);
    /**
     * 每隔5条存储数据库，实际使用中可以3000条，然后清理list ，方便内存回收
     */
    @Autowired
    DemoService demoService;
  
    private static final int BATCH_COUNT = 5;
    List<Map<Integer, String>> list = new ArrayList<Map<Integer, String>>();

    @Override
    public void invoke(Map<Integer, String> data, AnalysisContext context) {
        LOGGER.info("解析到一条数据:{}", JSON.toJSONString(data));
        list.add(data);
        if (list.size() >= BATCH_COUNT) {
            saveData();
            list.clear();
        }
    }

    @Override
    public void doAfterAllAnalysed(AnalysisContext context) {
        saveData();
        LOGGER.info("所有数据解析完成！");
    }

    /**
     * 加上存储数据库
     */
    private void saveData() {
        LOGGER.info("{}条数据，开始存储数据库！", list.size());
        demoService.save()
        LOGGER.info("存储数据库成功！");
    }
}
```



- [ ] [easyExcel的web用法](https://www.cnblogs.com/java-hardly-road/p/11136980.html)

- [ ] [@Autowired注入失效问题](https://blog.csdn.net/yuxielea/article/details/103986289)

- [ ] [spring的bean注入无效和new创建对象的区别](https://blog.csdn.net/qq_20009015/article/details/85055502)





