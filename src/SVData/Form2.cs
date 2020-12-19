using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using System.Linq;
using System.IO;
using System.Windows.Forms;
using HtmlAgilityPack;
using SpookVooper.Api.Entities;

namespace SVData
{
    public partial class GetData : Form
    {
        public GetData()
        {
            InitializeComponent();
        }

        private async void GetData_GetData_Click(object sender, EventArgs e)
        {
            List<string> urllist = new List<string>()
            {
                "https://spookvooper.com/user/search/a",
                "https://spookvooper.com/user/search/b",
                "https://spookvooper.com/user/search/c",
                "https://spookvooper.com/user/search/d",
                "https://spookvooper.com/user/search/e",
                "https://spookvooper.com/user/search/f",
                "https://spookvooper.com/user/search/g",
                "https://spookvooper.com/user/search/h",
                "https://spookvooper.com/user/search/i",
                "https://spookvooper.com/user/search/j",
                "https://spookvooper.com/user/search/k",
                "https://spookvooper.com/user/search/l",
                "https://spookvooper.com/user/search/m",
                "https://spookvooper.com/user/search/n",
                "https://spookvooper.com/user/search/o",
                "https://spookvooper.com/user/search/p",
                "https://spookvooper.com/user/search/q",
                "https://spookvooper.com/user/search/r",
                "https://spookvooper.com/user/search/s",
                "https://spookvooper.com/user/search/t",
                "https://spookvooper.com/user/search/u",
                "https://spookvooper.com/user/search/v",
                "https://spookvooper.com/user/search/w",
                "https://spookvooper.com/user/search/x",
                "https://spookvooper.com/user/search/y",
                "https://spookvooper.com/user/search/z",
                "https://spookvooper.com/user/search/0",
                "https://spookvooper.com/user/search/1",
                "https://spookvooper.com/user/search/2",
                "https://spookvooper.com/user/search/3",
                "https://spookvooper.com/user/search/4",
                "https://spookvooper.com/user/search/5",
                "https://spookvooper.com/user/search/6",
                "https://spookvooper.com/user/search/7",
                "https://spookvooper.com/user/search/8",
                "https://spookvooper.com/user/search/9",
                "https://spookvooper.com/user/search/,",
                "https://spookvooper.com/group/search/a",
                "https://spookvooper.com/group/search/b",
                "https://spookvooper.com/group/search/c",
                "https://spookvooper.com/group/search/d",
                "https://spookvooper.com/group/search/e",
                "https://spookvooper.com/group/search/f",
                "https://spookvooper.com/group/search/g",
                "https://spookvooper.com/group/search/h",
                "https://spookvooper.com/group/search/i",
                "https://spookvooper.com/group/search/j",
                "https://spookvooper.com/group/search/k",
                "https://spookvooper.com/group/search/l",
                "https://spookvooper.com/group/search/m",
                "https://spookvooper.com/group/search/n",
                "https://spookvooper.com/group/search/o",
                "https://spookvooper.com/group/search/p",
                "https://spookvooper.com/group/search/q",
                "https://spookvooper.com/group/search/r",
                "https://spookvooper.com/group/search/s",
                "https://spookvooper.com/group/search/t",
                "https://spookvooper.com/group/search/u",
                "https://spookvooper.com/group/search/v",
                "https://spookvooper.com/group/search/w",
                "https://spookvooper.com/group/search/x",
                "https://spookvooper.com/group/search/y",
                "https://spookvooper.com/group/search/z",
                "https://spookvooper.com/group/search/0",
                "https://spookvooper.com/group/search/1",
                "https://spookvooper.com/group/search/2",
                "https://spookvooper.com/group/search/3",
                "https://spookvooper.com/group/search/4",
                "https://spookvooper.com/group/search/5",
                "https://spookvooper.com/group/search/6",
                "https://spookvooper.com/group/search/7",
                "https://spookvooper.com/group/search/8",
                "https://spookvooper.com/group/search/9",
                "https://spookvooper.com/group/search/,"
            };
            List<string> allsvidlist = new List<string>();
            HtmlWeb hw = new HtmlWeb();
            GetData_Status.Text = "Getting SVIDs...";
            GetData_Progress.Maximum = 72;
            foreach (string url in urllist)
            {
                HtmlAgilityPack.HtmlDocument doc = hw.Load(url);
                foreach (HtmlNode link in doc.DocumentNode.SelectNodes("//a[@href]"))
                {
                    string rawnode = link.OuterHtml; ;
                    string[] rawsplit = rawnode.Split(">");
                    string linkcontent = rawsplit[0].Replace("<a href=", "");
                    if (linkcontent.Contains("svid="))
                    {
                        string svids = linkcontent.Replace("/User/Info?svid=", "");
                        string svid = svids.Replace("\"", "");
                        allsvidlist.Add(svid);
                    }
                    else if (linkcontent.Contains("groupid="))
                    {
                        string svids = linkcontent.Replace("/Group/View?groupid=", "");
                        string svid = svids.Replace("\"", "");
                        allsvidlist.Add(svid);
                    }
                }
                GetData_Progress.Increment(1);
            }
            var database = new Dictionary<string, Dictionary<string, Dictionary<string, dynamic>>>();
            List<string> distinctsvid = allsvidlist.Distinct().ToList();
            distinctsvid.Sort();
            GetData_Status.Text = "Getting Data...";
            GetData_Progress.Value = 0;
            GetData_Progress.Maximum = distinctsvid.Count;
            foreach (string svid in distinctsvid)
            {
                if (svid.StartsWith("u-"))
                {
                    User u = new User(svid);
                    UserSnapshot snapShot = await u.GetSnapshotAsync();

                    string date = DateTime.Now.ToString("dd-MM-yy");
                    database[svid] = new Dictionary<string, Dictionary<string, object>>();
                    database[svid][date] = new Dictionary<string, object>();
                    database[svid][date]["api use count"] = snapShot.api_use_count;
                    database[svid][date]["comment likes"] = snapShot.comment_likes;
                    database[svid][date]["credits"] = snapShot.credits;
                    database[svid][date]["description"] = snapShot.description;
                    database[svid][date]["discord ban count"] = snapShot.discord_ban_count;
                    database[svid][date]["discord commends"] = snapShot.discord_commends;
                    database[svid][date]["discord commends sent"] = snapShot.discord_commends_sent;
                    database[svid][date]["discord game xp"] = snapShot.discord_game_xp;
                    database[svid][date]["discord id"] = snapShot.discord_id;
                    database[svid][date]["discord kick count"] = snapShot.discord_kick_count;
                    database[svid][date]["discord last commend hour"] = snapShot.discord_last_commend_hour;
                    database[svid][date]["discord last commend message"] = snapShot.discord_last_commend_message;
                    database[svid][date]["discord last message minute"] = snapShot.discord_last_message_minute;
                    database[svid][date]["discord message count"] = snapShot.discord_message_count;
                    database[svid][date]["discord message xp"] = snapShot.discord_message_xp;
                    database[svid][date]["discord warning count"] = snapShot.discord_warning_count;
                    database[svid][date]["district"] = snapShot.district;
                    database[svid][date]["id"] = snapShot.Id;
                    database[svid][date]["image url"] = snapShot.image_url;
                    database[svid][date]["minecraft id"] = snapShot.minecraft_id;
                    database[svid][date]["name"] = snapShot.UserName;
                    database[svid][date]["nationstate"] = snapShot.nationstate;
                    database[svid][date]["post likes"] = snapShot.post_likes;
                    database[svid][date]["twitch id"] = snapShot.twitch_id;
                    database[svid][date]["twitch last message minute"] = snapShot.twitch_last_message_minute;
                    database[svid][date]["twitch messages"] = snapShot.twitch_messages;
                    database[svid][date]["twitch message xp"] = snapShot.twitch_message_xp;
                    GetData_Progress.Increment(1);
                }
                else if (svid.StartsWith("g-"))
                {
                    SpookVooper.Api.Entities.Groups.Group g = new SpookVooper.Api.Entities.Groups.Group(svid);
                    GroupSnapshot snapShot = await g.GetSnapshotAsync();

                    string date = DateTime.Now.ToString("dd-MM-yy");
                    database[svid] = new Dictionary<string, Dictionary<string, object>>();
                    database[svid][date] = new Dictionary<string, object>();
                    database[svid][date]["credits"] = snapShot.Credits;
                    database[svid][date]["credits invested"] = snapShot.Credits_Invested;
                    database[svid][date]["default role id"] = snapShot.Default_Role_Id;
                    database[svid][date]["description"] = snapShot.Description;
                    database[svid][date]["district"] = snapShot.District_Id;
                    database[svid][date]["category"] = snapShot.Group_Category;
                    database[svid][date]["image url"] = snapShot.Image_Url;
                    database[svid][date]["name"] = snapShot.Name;
                    database[svid][date]["id"] = snapShot.Id;
                    database[svid][date]["open"] = snapShot.Open;
                    database[svid][date]["owner id"] = snapShot.Owner_Id;
                    GetData_Progress.Increment(1);
                }
            }
            GetData_Status.Text = "Updating database.json...";
            string json = JsonConvert.SerializeObject(database, Formatting.Indented);
            using (TextWriter tw = new StreamWriter("SVData/database.json"))
            {
                tw.Write(json);
            }
            GetData_Status.Text = "Completed!";

        }

        private void GetData_Cancel_Click(object sender, EventArgs e)
        {
            this.Close();
            var MainWindow = new Main();
            MainWindow.Show();
        }
    }
}
